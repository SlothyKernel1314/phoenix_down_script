import logging
from logging.handlers import RotatingFileHandler
from utilities import *


logger_application_name = "logger"


# LOGGER CONFIGURATION -------------------------------------------------------------------------------------------------

# creation of the logger object that we will use to write in the logs
logger = logging.getLogger()

# set level logger to DEBUG for get all traces
logger.setLevel(logging.INFO)

# creation of the formatter
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] : %(message)s')

file_name = create_timestamped_and_named_file_name(logger_application_name)

# creation of the first handler which redirect traces to a log file
file_handler = RotatingFileHandler(PD_SCRIPT_ROOT_LOGS_PATH + "/" + logger_application_name + '/'
                                   + file_name, 'a', 1000000, 1)
# set level of the first handler to DEBUG
file_handler.setLevel(logging.INFO)
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


# LOGGER SCRIPT --------------------------------------------------------------------------------------------------------


def logger_script():
    latest_logger_file = get_the_latest_file_in_a_folder(PD_SCRIPT_ROOT_LOGS_PATH + "/" + logger_application_name)

    # opens the file for reading only in binary format in order to upload
    file = open(latest_logger_file, "rb")

    upload_file_to_server_ftp_without_logging_messages(file, file_name, logger_application_name)

    file.close()
