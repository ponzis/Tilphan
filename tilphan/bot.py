import logging

import discord

from tilphan.managers.extension_manager import ExtensionManagers

logger = logging.getLogger(__name__)


class TilphanBot(ExtensionManagers, discord.Client):
    '''
    This is the pre-made bot that contains all of the required modules to run plugins.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.load_extension_folder('tilphan/extensions/')

    def run(self, token):
        try:
            super().run(token)
        except:
            pass
        finally:
            logger.info('The program has closed.')

    async def close(self):
        await super().close()
        logger.info("The bot has closed")

    async def on_ready(self):
        logging.info(f"Bot started up {self.user.name}:{self.user.id}")
