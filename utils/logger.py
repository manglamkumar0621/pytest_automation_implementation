"""Generates log"""
from datetime import datetime
import logging
import os.path

class LoggerSingleton:
    __logger = None

    @staticmethod
    def get_logger():
        """
        Create logger with default configuration and add level.
        Set format for log using file handler
        """
        if LoggerSingleton.__logger is None:
            log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
            os.makedirs(log_dir, exist_ok=True)
            log_path = os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
            #log_path = os.path.join(log_dir, "test_log.log")

            logger = logging.getLogger("SaucedemoTest")
            logger.setLevel(logging.DEBUG)
            if not logger.handlers:
                fh = logging.FileHandler(log_path)
                formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
                fh.setFormatter(formatter)
                logger.addHandler(fh)

                console_handler = logging.StreamHandler()
                console_handler.setFormatter(formatter)
            LoggerSingleton.__logger = logger
        return LoggerSingleton.__logger
