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
from setup_logger import logger


# SAMPLE REQUESTS ------------------------------------------------------------------------------------------------------

# get_board_by_id_sample_version(TRELLO_MBL_BOARD_ID)
# get_open_cards_by_board_id_sample_version(TRELLO_MBL_BOARD_ID)
# get_card_by_id_sample_version(TRELLO_CH_CARD_ID)
# get_boards_by_member_username_sample_version(TRELLO_MEMBER_USERNAME)


# MAIN SCRIPT ----------------------------------------------------------------------------------------------------------

# TODO : gérer exceptions (erreurs)
# TODO : alertes en cas d'erreur + envoi de fichier de log (mail, trello)

logging.info('Phoenix Down Script started !')

# If the root path directory of phoenix down script doesn't exist yet...
# ... creation of this directory
logging.info("creating the root path directory of Phoenix Down Script...")
create_directory(PD_SCRIPT_ROOT_PATH)

ts = TrelloScript()
ts.run_script()

# fs = FirefoxScript()
# fs.run_script()

js = JdownloaderScript()
js.run_script()

logging.info('Phoenix Down Script finished !')
