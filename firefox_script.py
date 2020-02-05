import os
import shutil
from constants import *
from utilities import *


# VARIABLES ------------------------------------------------------------------------------------------------------------

application_name = "firefox"


# SCRIPT ---------------------------------------------------------------------------------------------------------------

# goal : upload a zip archive to the server, save (large) files locally

def firefox_script():
    # If the work directory "../firefox" doesn't existe yet...
    # ... creation of this directory
    create_directory(PD_SCRIPT_ROOT_PATH + "/" + application_name)

    # creation of timestamped directory
    timestamped_directory = create_timestamped_directory()

    # Designation of firefox profile directory as current directory
    os.chdir(FIREFOX_PROFILE_DIRECTORY_PATH)

    # copying local places.sqlite (firefox profile) to phoenix down script firefox directory
    shutil.copy(FIREFOX_PLACES_SQLITE_FILE_NAME, PD_SCRIPT_ROOT_PATH + "/" + application_name + "/"
                + str(timestamped_directory))

    # copying local favicons.sqlite (firefox profile) to phoenix down script firefox directory
    shutil.copy(FIREFOX_FAVICONS_SQLITE_FILE_NAME, PD_SCRIPT_ROOT_PATH + "/" + application_name + "/"
                + str(timestamped_directory))

    # get the latest file in bookmarkbackups directory in order to save a JSON encrypted backup of Firefox bookmarks
    bookback_file = get_the_latest_file_in_a_folder(FIREFOX_PROFILE_DIRECTORY_PATH +
                                                    "/" + FIREFOX_BOOKMARKBACKUPS_FOLDER)

    # copying local "bookback_file" (firefox profile) to phoenix down script firefox directory
    shutil.copy(bookback_file, PD_SCRIPT_ROOT_PATH + "/" + application_name + "/"
                + str(timestamped_directory))

    # get all files paths in log (timestamped) diectory in order to zip theses files + server upload
    files_paths_to_zip = get_all_file_paths(PD_SCRIPT_ROOT_PATH + "/" + application_name + "/"
                              + str(timestamped_directory))

# TODO : zip files and upload archive to server, then, delete archive
