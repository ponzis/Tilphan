# TODO create the config system

import json

extension_folders = ['tilphan.extensions']


def load_config(path):
    with open(path) as config_file:
        config = json.load(config_file)
        return config
