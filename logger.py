import logging
import sys
import traceback
from typing import Callable


class FileIsNotLogError(Exception):
    pass

class Logger:
    FORMAT = '%(levelname)-8s %(message)s'
    def __init__(self, file_name:str) -> None:

        if ".log" not in file_name:
            raise FileIsNotLogError(f"{file_name} is not a valid log file (.log)")

        self.logger = self.__get_logger(file_name)

    def __get_logger(self, file_name:str) -> logging.Logger:
        # create logger with 'file_name'
        logger = logging.getLogger(f"{file_name}")
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        file_handler = logging.FileHandler(f"{file_name}")
        file_handler.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        # create formatter and add it to the handlers
        formatter = logging.Formatter(self.FORMAT)
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        return logger
    
    def debug(self, msg: str) -> None:
        self.logger.debug(msg)
