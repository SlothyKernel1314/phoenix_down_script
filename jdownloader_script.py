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

        # If the work directory "../jdownloader" doesn't existe yet...
        # ... creation of this directory
        create_directory(PD_SCRIPT_ROOT_PATH + "/" + self.application_name)

        # creation of timestamped subdirectory
        timestamped_directory = create_timestamped_directory()

        # designation of jdownloader cfg directory as current directory
        os.chdir(JDOWNLOADER_CFG_DIRECTORY_PATH)

        logging.info('getting latest downloadList*.zip file')

        # get latest downloadList*.zip file
        dlzip_file = get_max_file_name_with_wildcard("downloadList*.zip")

        logging.info('adding latest downloadList*.zip file to files list to backup')

        # add downloadList*.zip file to files list to backup
        self.files_list_to_backup.append(dlzip_file)

        logging.info('getting latest linkcollector*.zip file')

        # get latest linkcollector*.zip file
        lnkcoll_file = get_max_file_name_with_wildcard("linkcollector*.zip")

        logging.info('adding latest linkcollector*.zip file to files list to backup')

        # add linkcollector*.zip file to files list to backup
        self.files_list_to_backup.append(lnkcoll_file)

        # get the path of log directory
        directory_log_path = PD_SCRIPT_ROOT_PATH + "/" + self.application_name + "/" + str(timestamped_directory)

        logging.info('copying local files (in order to backup) to phoenix down script firefox directory...')

        # copying local files (in order to backup) to phoenix down script firefox directory
        for file in self.files_list_to_backup:
            shutil.copy(file, directory_log_path)

        logging.info('copy done')

        logging.info('get all files in order to zip theses files')

        # get all files paths in log (timestamped) diectory in order to zip theses files + server upload
        file_paths_to_zip = get_all_file_paths(directory_log_path)

        logging.info('zipping all files...')

        # zip all files
        zip_file = zip_files(file_paths_to_zip, directory_log_path, JDOWNLOADER_ZIP_FILE_BASENAME)

        logging.info('zip done')

        # opens the zip file for reading only in binary format in order to upload
        opened_zip_file = open(zip_file.filename, "rb")

        logging.info('uploading all files...')

        # upload zip to ftp server
        upload_file_to_server_ftp(opened_zip_file, zip_file.filename, self.application_name)

        logging.info('upload done')

        logging.info('deleting local zip file...')

        # delete local zip file
        os.remove(zip_file.filename)

        logging.info('delete local zip file done')

        logging.info('save all files locally + upload zip files to ftp server : success !')

        logging.info('jdownloader script is terminated')
