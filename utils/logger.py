"""Generates log"""
import logging

def get_logger():
    """
    Create logger with default configuration and add level.
    Set format for log using file handler
    """
    logger = logging.getLogger("AmazonTest")
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("logs/AmazonTestLog.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger
