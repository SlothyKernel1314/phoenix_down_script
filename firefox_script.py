# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
import shutil
from constants import *
from utilities import *

# goal : upload a zip archive to the server, save (large) files locally


class FirefoxScript:
    def __init__(self):
        self.application_name = "firefox"

    def run_script(self):

        logging.info('firefox script is running...')

        # if the work directory "../firefox" doesn't existe yet...
        # ... creation of this directory
        create_directory(PD_SCRIPT_ROOT_PATH + "/" + self.application_name)

        # creation of timestamped directory
        timestamped_directory = create_timestamped_directory()

        # designation of firefox profile directory as current directory
        os.chdir(FIREFOX_PROFILE_DIRECTORY_PATH)

        # get the path of log directory
        directory_log_path = PD_SCRIPT_ROOT_PATH + "/" + self.application_name + "/" + str(timestamped_directory)

        logging.info('copying local places.sqlite (firefox profile) to phoenix down script firefox directory')

        # copying local places.sqlite (firefox profile) to phoenix down script firefox directory
        shutil.copy(FIREFOX_PLACES_SQLITE_FILE_NAME, directory_log_path)

        logging.info('copying local favicons.sqlite (firefox profile) to phoenix down script firefox directory')

        # copying local favicons.sqlite (firefox profile) to phoenix down script firefox directory
        shutil.copy(FIREFOX_FAVICONS_SQLITE_FILE_NAME, directory_log_path)

        # get the latest file in bookmarkbackups directory in order to save a JSON encrypted backup of Firefox bookmarks
        bookback_file = get_the_latest_file_in_a_folder(FIREFOX_PROFILE_DIRECTORY_PATH +
                                                        "/" + FIREFOX_BOOKMARKBACKUPS_FOLDER)

        logging.info('copying local "bookback_file" (firefox profile) to phoenix down script firefox directory')

        # copying local "bookback_file" (firefox profile) to phoenix down script firefox directory
        shutil.copy(bookback_file, directory_log_path)

        # get all files paths in log (timestamped) diectory in order to zip theses files + server upload
        file_paths_to_zip = get_all_file_paths(directory_log_path)

        logging.info('zipping all files (places, favicons, bookback)...')

        # zip all files
        zip_file = zip_files(file_paths_to_zip, directory_log_path, FIREFOX_ZIP_FILE_BASENAME)

        logging.info('zip done')

        # opens the zip file for reading only in binary format in order to upload
        opened_zip_file = open(zip_file.filename, "rb")

        logging.info('uploading the zip to ftp server...')

        # upload zip to ftp server
        upload_file_to_server_ftp(opened_zip_file, zip_file.filename, self.application_name)

        logging.info('upload done')

        logging.info('deleting local zip file...')

        # delete local zip file
        os.remove(zip_file.filename)

        logging.info('delete local zip done')

        logging.info('save all files locally + upload zip files to ftp server : success !')

        logging.info('firefox script is terminated')
