import logging

class logg:

    #Creating log file
    def make_logfile():
        logging.basicConfig(filename='logname',
                                filemode='a',
                                format='%(asctime)s %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG)
    #Writing into log file
    def write_into_file(error):
        logging.debug(error)
