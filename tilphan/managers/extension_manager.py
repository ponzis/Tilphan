"""
This module will handel all of the plugins
"""
import asyncio
import importlib.util
import inspect
import logging
import os

import sys
from os.path import isfile

logger = logging.getLogger(__name__)


def _is_submodule(parent, child):
    return parent == child or child.startswith(parent + ".")


class ExtensionManagers:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra_events = {}
        self.extensions = {}
        self.plugins = {}

    def dispatch(self, event_name, *args, **kwargs):
        super().dispatch(event_name, *args, **kwargs)
        ev = 'on_' + event_name
        for event in self.extra_events.get(ev, []):
            coro = self._run_event(event, event_name, *args, **kwargs)
            asyncio.ensure_future(coro, loop=self.loop)

    def add_listener(self, func, name=None):
        name = func.__name__ if name is None else name

        if not asyncio.iscoroutinefunction(func):
            raise AttributeError('Listeners must be coroutines')

        if name in self.extra_events:
            self.extra_events[name].append(func)
        else:
            self.extra_events[name] = [func]

    def remove_listener(self, func, name=None):
        name = func.__name__ if name is None else name

        if name in self.extra_events:
            try:
                self.extra_events[name].remove(func)
            except ValueError:
                pass

    def load_extension_folder(self, path):
        print(path)

        for file in os.listdir(path):
            if not isfile(file) and file.endswith('.py') and not file.startswith('_'):
                name = f'plugin.{file[:-3]}'
                if name in self.extensions:
                    continue

                spec = importlib.util.spec_from_file_location(name, os.path.join(path, file))
                lib = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(lib)
                self._load_extension(lib, lib.__name__)

    def unload_extension_folder(self, path):
        for file in os.listdir(path):
            if not isfile(file) and file.endswith('.py') and not file.startswith('_'):
                self.unload_extension(f'plugin.{file[:-3]}')

    def load_extension(self, name):
        if name in self.extensions:
            return

        lib = importlib.import_module(name)
        self._load_extension(lib, name)

    def _load_extension(self, lib, name):

        if not hasattr(lib, 'setup'):
            del lib
            # if name in sys.modules:
            del sys.modules[name]

            raise AttributeError('The plugin has no setup function.')

        lib.setup(self)
        logger.info(f'startup {name}')
        self.extensions[name] = lib

    def unload_extension(self, name):
        lib = self.extensions[name]
        if lib is None:
            return

        lib_name = lib.__name__

        try:
            func = getattr(lib, 'teardown')
        except AttributeError:
            pass
        else:
            try:
                func(self)
            except:
                pass
        finally:

            del lib
            del self.extensions[name]
            del sys.modules[name]
            for module in list(sys.modules.keys()):
                if _is_submodule(lib_name, module):
                    del sys.modules[module]
            logger.info(f'teardown {name}')

    def register_plugin(self, plugin):
        self.plugins[type(plugin).__name__] = plugin

        members = inspect.getmembers(plugin)
        for name, member in members:
            # register event listeners from the plugin
            if name.startswith('on_'):
                self.add_listener(member, name)

    def unregister_plugin(self, name):
        plugin = self.plugins.pop(name, None)
        if plugin is None:
            return

        members = inspect.getmembers(plugin)
        for name, member in members:
            # remove event listeners from plugin
            if name.startswith('on_'):
                self.remove_listener(member)

        unloader_name = f'_{plugin.__class__.__name__}__unload'
        try:
            unloader = getattr(plugin, unloader_name)
        except AttributeError:
            pass
        else:
            unloader()

        del plugin

    async def close(self):
        logging.info('Unloading all of the extensions.')
        for extension in tuple(self.extensions):
            try:
                self.unload_extension(extension)
            except:
                pass

        for plugin in tuple(self.plugins):
            try:
                self.unregister_plugin(plugin)
            except:
                pass

        await super().close()
