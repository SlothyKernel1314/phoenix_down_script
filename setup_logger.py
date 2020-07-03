import logging
from logging.handlers import RotatingFileHandler
from utilities import *

# VARIABLES ------------------------------------------------------------------------------------------------------------

log_folder_name = "log"


# LOGGER CONFIGURATION -------------------------------------------------------------------------------------------------

# creation of the logger object that we will use to write in the logs
logger = logging.getLogger()

# set level logger to DEBUG for get all traces
logger.setLevel(logging.DEBUG)

# creation of the formatter
formatter = logging.Formatter('[%(levelname)s] : %(asctime)s %(message)s')

# creation of the first handler which redirect traces to a log file
file_handler = RotatingFileHandler(PD_SCRIPT_ROOT_PATH + "/" + log_folder_name + '/'
                                   + create_timestamped_and_named_file("logger"), 'a', 1000000, 1)
# set level of the first handler to DEBUG
file_handler.setLevel(logging.DEBUG)
# use formatter for set first handler file name generation
file_handler.setFormatter(formatter)
# add the first handler to the logger
logger.addHandler(file_handler)

# creation of a second handler which redirect traces to the console
stream_handler = logging.StreamHandler()
# # set level of the second handler to DEBUG
stream_handler.setLevel(logging.DEBUG)
# add the second handler to the logger
logger.addHandler(stream_handler)