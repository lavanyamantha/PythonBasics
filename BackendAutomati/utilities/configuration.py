import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')

    return config

def getpassword():
    return "Ganesh$5"