#            )                              (                                                   )
#         ( /(         (        (      )    )\ )      (  (                    (   (          ( /(
#  `  )   )\())  (    ))\  (    )\  ( /(   (()/(  (   )\))(    (      (    (  )(  )\  `  )   )\())
#  /(/(  ((_)\   )\  /((_) )\ )((_) )\())   ((_)) )\ ((_)()\   )\ )   )\   )\(()\((_) /(/(  (_))/
# ((_)_\ | |(_) ((_)(_))  _(_/( (_)((_)\    _| | ((_)_(()((_) _(_/(  ((_) ((_)((_)(_)((_)_\ | |_
# | '_ \)| ' \ / _ \/ -_)| ' \))| |\ \ /  / _` |/ _ \\ V  V /| ' \)) (_-</ _|| '_|| || '_ \)|  _|
# | .__/ |_||_|\___/\___||_||_| |_|/_\_\  \__,_|\___/ \_/\_/ |_||_|  /__/\__||_|  |_|| .__/  \__|
# |_|


# Author :
# +-+-+-+-+-+-+-+-+-+
# |I|A|m|T|e|r|r|o|r|
# +-+-+-+-+-+-+-+-+-+

# Licence :
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

# Notes :
# Python script tested on Ubuntu Linux. It can run on Windows with minor adjustements.


########################################################################################################################

########################################################################################################################

# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from trello_sample import *
from constants import *
from trello_script import *
from firefox_script import *
from jdownloader_script import *


# VARIABLES ------------------------------------------------------------------------------------------------------------

log_folder_name = "log"


# SAMPLE REQUESTS ------------------------------------------------------------------------------------------------------

# get_board_by_id_sample_version(TRELLO_MBL_BOARD_ID)
# get_open_cards_by_board_id_sample_version(TRELLO_MBL_BOARD_ID)
# get_card_by_id_sample_version(TRELLO_CH_CARD_ID)
# get_boards_by_member_username_sample_version(TRELLO_MEMBER_USERNAME)


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


# MAIN SCRIPT ----------------------------------------------------------------------------------------------------------

logging.info('Phoenix Down Script started !')

# If the root path directory of phoenix down script doesn't exist yet...
# ... creation of this directory
logging.info("creation of the root path directory of Phoenix Down Script...")
create_directory(PD_SCRIPT_ROOT_PATH)

ts = TrelloScript()
ts.trello_script()

# fs = FirefoxScript()
# fs.firefox_script()

# js = JdownloaderScript()
# js.jdownloader_script()

logging.info('Phoenix Down Script finished !')
