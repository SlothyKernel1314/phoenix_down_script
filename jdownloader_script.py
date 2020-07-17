# -*- coding: utf-8 -*-
# !/usr/bin/env python

from utilities import *
import shutil


class JdownloaderScript:
    def __init__(self):
        self.application_name = "jdownloader"
        self.files_list_to_backup = []

    def run_script(self):

        logging.info('jdownloader script is running...')

        create_directory(PD_SCRIPT_ROOT_PATH + "/" + self.application_name)

        timestamped_directory = create_timestamped_directory()

        os.chdir(JDOWNLOADER_CFG_DIRECTORY_PATH)

        logging.info('getting latest downloadList*.zip file')
        dlzip_file = get_max_file_name_with_wildcard("downloadList*.zip")

        logging.info('adding latest downloadList*.zip file to files list to backup')
        self.files_list_to_backup.append(dlzip_file)

        logging.info('getting latest linkcollector*.zip file')
        lnkcoll_file = get_max_file_name_with_wildcard("linkcollector*.zip")

        logging.info('adding latest linkcollector*.zip file to files list to backup')
        self.files_list_to_backup.append(lnkcoll_file)

        backup_directory_path = PD_SCRIPT_ROOT_PATH + "/" + self.application_name + "/" + str(timestamped_directory)

        logging.info('copying local files (in order to backup) to phoenix down script firefox directory...')
        for file in self.files_list_to_backup:
            shutil.copy(file, backup_directory_path)

        logging.info('copy done')

        logging.info('get all files in order to zip theses files')
        file_paths_to_zip = get_all_file_paths(backup_directory_path)

        zip_file = zip_files(file_paths_to_zip, backup_directory_path, JDOWNLOADER_ZIP_FILE_BASENAME)

        # opens the zip file for reading only in binary format in order to upload
        opened_zip_file = open(zip_file.filename, "rb")

        upload_file_to_server_ftp(opened_zip_file, zip_file.filename, self.application_name)

        logging.info('deleting local zip file...')
        os.remove(zip_file.filename)

        logging.info('delete local zip file done')

        logging.info('jdownloader script is terminated')
