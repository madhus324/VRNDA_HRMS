# import inspect
# import logging
#
# import pytest
# import pytest_html
#
#
# class LogGen:
#     def loggen(logLevel=logging.DEBUG):
#         # Set class/method name from where its called
#         logger_name = inspect.stack()[1][3]
#         # create logger
#         logger = logging.getLogger(logger_name)
#         logger.setLevel(logLevel)
#         # create console handler or file handler and set the log level
#         fh = logging.FileHandler("Syscon.log", mode='a')
#         # create formatter - how you want your logs to be formatted
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
#                                       datefmt='%m/%d/%Y %I:%M:%S %p')
#         # add formatter to console or file handler
#         fh.setFormatter(formatter)
#         # add console handler to logger
#         logger.addHandler(fh)
#         return logger
#
#

import logging
import os

# Create a logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/test_log.log'),  # Log to a file
        logging.StreamHandler()  # Log to console
    ]
)
