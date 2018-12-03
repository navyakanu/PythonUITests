import configparser
import os

import sys


class ConfigSetup:
    def __init__(self):
        self.__configuration = configparser.ConfigParser()

        self.ROOT_DIR = os.path.dirname(sys.modules['src'].__file__)
        CONFIG_FILE_PATH = os.path.join(self.ROOT_DIR, 'config.ini')

        self.__configuration.read(CONFIG_FILE_PATH)

    def get_property(self, propertyName):
        return str(self.__configuration.get("local", propertyName))

    def get_base_url(self):
        baseUrl = self.get_property("url")
        return baseUrl
