from configparser import ConfigParser
from exceptions import MissingKeyException

class ConfigurationService():
    """ Init the configuration file from be used through the proyect"""

    def __init__(self, enviroment):
        """Init the configuration object """

        self.config = ConfigParser()
        self.config.read('config.ini')
        self.enviroment = enviroment

    def return_value(self, value):
        """Return a value from a config"""

        if value in self.config[self.enviroment]:

            return self.config[self.enviroment][value]
            
        else:

            raise MissingKeyException()