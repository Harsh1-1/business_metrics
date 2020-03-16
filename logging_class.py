import logging

# This class can be made singleton
class Logg:

    #TODO constructor can be used to initialize log file name 
    def __init__(self):
        pass

    #Creates log file
    @staticmethod
    def make_logfile():
        logging.basicConfig(filename='logname',
                                filemode='a',
                                format='%(asctime)s %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG)

    #TODO log based on logging level
    #Writing into log file
    @staticmethod
    def write_into_file(error):
        logging.debug(error)
