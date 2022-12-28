import configparser

config= configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('common info','baseURL')
        return url
    @staticmethod
    def getUserMail():
        username = config.read('common info','usermail')
        return username
    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password
