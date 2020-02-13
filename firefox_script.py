import os
import shutil
from constants import *
from utilities import *


# VARIABLES ------------------------------------------------------------------------------------------------------------

application_name = "firefox"


# SCRIPT ---------------------------------------------------------------------------------------------------------------

# goal : upload a zip archive to the server, save (large) files locally

def firefox_script():
    # if the work directory "../firefox" doesn't existe yet...
    # ... creation of this directory
    create_directory(PD_SCRIPT_ROOT_PATH + "/" + application_name)

    # creation of timestamped directory
    timestamped_directory = create_timestamped_directory()

    # designation of firefox profile directory as current directory
    os.chdir(FIREFOX_PROFILE_DIRECTORY_PATH)

    directory_log_path = PD_SCRIPT_ROOT_PATH + "/" + application_name + "/" + str(timestamped_directory)

    # copying local places.sqlite (firefox profile) to phoenix down script firefox directory
    shutil.copy(FIREFOX_PLACES_SQLITE_FILE_NAME, directory_log_path)

    # copying local favicons.sqlite (firefox profile) to phoenix down script firefox directory
    shutil.copy(FIREFOX_FAVICONS_SQLITE_FILE_NAME, directory_log_path)

    # get the latest file in bookmarkbackups directory in order to save a JSON encrypted backup of Firefox bookmarks
    bookback_file = get_the_latest_file_in_a_folder(FIREFOX_PROFILE_DIRECTORY_PATH +
                                                    "/" + FIREFOX_BOOKMARKBACKUPS_FOLDER)

    # copying local "bookback_file" (firefox profile) to phoenix down script firefox directory
    shutil.copy(bookback_file, directory_log_path)

    # get all files paths in log (timestamped) diectory in order to zip theses files + server upload
    file_paths_to_zip = get_all_file_paths(directory_log_path)

    # zip all files
    zip_file = zip_files(file_paths_to_zip, directory_log_path, FIREFOX_ZIP_FILE_BASENAME)

    # opens the zip file for reading only in binary format in order to upload
    opened_zip_file = open(zip_file.filename, "rb")

    # upload zip to ftp server
    # upload_file_to_server_ftp(opened_zip_file, zip_file.filename, application_name)

# TODO : tester que l'upload fonctionne bien en passant un micro fichier en dur, rm le zip local
