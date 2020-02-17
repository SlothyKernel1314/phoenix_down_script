from utilities import *


# VARIABLES ------------------------------------------------------------------------------------------------------------

application_name = "jdownloader"


# SCRIPT ---------------------------------------------------------------------------------------------------------------

def jdownloader_script():
    # If the work directory "../trello" doesn't existe yet...
    # ... creation of this directory
    create_directory(PD_SCRIPT_ROOT_PATH + "/" + application_name)

    # creation of timestamped directory
    timestamped_directory = create_timestamped_directory()
