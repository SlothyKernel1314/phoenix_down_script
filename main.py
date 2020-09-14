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


########################################################################################################################

########################################################################################################################

# !/usr/bin/python
# -*- coding: utf-8 -*-

from mother_of_all_scripts import *
from alerts import *

logging.info(PD_SCRIPT_STARTING_MESSAGE)

try:
    mother_of_all_scripts()
    logging.info(PD_SCRIPT_ENDING_MESSAGE)
except Exception as e:
    logging.error("The program ended unexpectedly !")
    logging.error("Error: " + str(e))

logger_script()

alm = Alerts()
alm.run_script()

# TODO : unit tests (constants / credentials errors, files ok in case or fail script, errors / warnings messages when
# logger throw e / w...)
# TODO : discord implementation with discord.py
# TODO : constants.py and #credentials.py example
# TODO : github description
