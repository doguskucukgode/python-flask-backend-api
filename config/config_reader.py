import configparser
import sys
from termcolor import colored


class ConfigReader:
    app_config_section = 'app-config'
    config_file_path = './config.cfg'
    config_parser = None

    def __init__(self, **kwargs):
        self.config_parser = configparser.ConfigParser()
        found = self.config_parser.read(self.config_file_path)
        if not found:
            print(colored('Config file: {} not found!'.format(self.config_file_path), 'red'))
            sys.exit()

    def get_app_config(self, conf_name):
        return self.config_parser.get(self.app_config_section, conf_name)
