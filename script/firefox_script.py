# -*- coding: utf-8 -*-
# !/usr/bin/env python

import shutil
from utilities import *


# goal : upload a zip archive to the server, save (large) files locally


class FirefoxScript:

    def __init__(self):
        self.application_name = "firefox"

    def run_script(self):
        logging.info('firefox script is running...')

        create_directory(PD_SCRIPT_ROOT_LOGS_PATH + "/" + self.application_name)

        timestamped_subdirectory = create_timestamped_directory()

        os.chdir(FIREFOX_PROFILE_DIRECTORY_PATH)

        backup_directory_path = PD_SCRIPT_ROOT_LOGS_PATH + "/" + self.application_name + "/" + str(
            timestamped_subdirectory)

        logging.info('copying local places.sqlite (firefox profile) to phoenix down script firefox directory')
        shutil.copy(FIREFOX_PLACES_SQLITE_FILE_NAME, backup_directory_path)

        logging.info('copying local favicons.sqlite (firefox profile) to phoenix down script firefox directory')
        shutil.copy(FIREFOX_FAVICONS_SQLITE_FILE_NAME, backup_directory_path)

        # get the latest file in bookmarkbackups directory in order to save a JSON encrypted backup of Firefox bookmarks
        bookback_file = get_the_latest_file_in_a_folder(FIREFOX_PROFILE_DIRECTORY_PATH +
                                                        "/" + FIREFOX_BOOKMARKBACKUPS_FOLDER)

        logging.info('copying local "bookback_file" (firefox profile) to phoenix down script firefox directory')
        shutil.copy(bookback_file, backup_directory_path)

        file_paths_to_zip = get_all_file_paths(backup_directory_path)

        zip_file = zip_files(file_paths_to_zip, backup_directory_path, FIREFOX_ZIP_FILE_BASENAME)

        # open the zip file for reading only in binary format in order to upload
        opened_zip_file = open(zip_file.filename, "rb")

        upload_file_to_server_ftp(opened_zip_file, zip_file.filename, self.application_name)

        logging.info('deleting local zip file...')
        os.remove(zip_file.filename)

        logging.info('delete local zip done')

        logging.info('firefox script is terminated')
