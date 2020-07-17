# -*- coding: utf-8 -*-
# !/usr/bin/env python

from credentials import *
from constants import *
import logging
import os
import time
import glob
import ftplib
from ftplib import FTP
from zipfile import ZipFile, ZIP_DEFLATED


def create_directory(path):
    logging.info('creating the folder ' + path + "...")
    if not os.path.isdir(path):
        os.makedirs(path)
        logging.info("the folder " + path + " was successfully created")
    else:
        logging.info("the folder " + path + " already exists, it's ok")

    # Designation of the working directory as current directory
    os.chdir(path)


def create_timestamped_directory():
    current_date = time.strftime("%Y%m%d")
    current_time = time.strftime("%H%M%S")
    format_directory_name = current_date + "_" + current_time
    logging.info('creating the folder ' + format_directory_name + "...")
    os.mkdir(format_directory_name)
    logging.info("the folder " + format_directory_name + " was successfully created")
    return format_directory_name


def create_timestamped_and_named_file_name(application_name):
    current_date = time.strftime("%Y%m%d")
    current_time = time.strftime("%H%M%S")
    format_file_name = current_date + "_" + current_time + "_" + application_name + "_log_phoenix_down.txt"
    return format_file_name


def upload_file_to_server_ftp(file, filename, application_name):
    ftp = FTP(SEEDBOX_DOMAIN_NAME)  # connect to host, default port
    try:
        logging.info("trying to connect the ftp server...")
        ftp.login(user=SEEDBOX_USER_NAME, passwd=SEEDBOX_PASSWD)  # login with credentials
        logging.info('ftp connection succeed !')
        try:
            # TODO : se placer dans le bon repertoire (ok) du serveur et creer un dossier *nom application* s'il n'existe pas
            # ftp.mkd(SEEDBOX_ROOT_PD_SCRIPT_PATH)
            # ftp.cwd(SEEDBOX_ROOT_PD_SCRIPT_PATH)
            # ftp.mkd(SEEDBOX_ROOT_PD_SCRIPT_PATH + "/" + application_name)
            ftp.cwd(SEEDBOX_ROOT_PD_SCRIPT_PATH + "/" + application_name)  # Set the current directory on the server
            logging.info('sending ' + filename + ' file to the ftp server... (' + application_name + ' file)')
            ftp.storbinary('STOR ' + filename + '', file)  # uploading file to the server
            logging.info('zip ' + filename + ' uploaded successfully!')
            ftp.retrlines('LIST') # TODO : remove in prod
        except ftplib.all_errors:
            logging.warning('unable to make directories')
    except ftplib.all_errors:
        logging.warning('unable to connect to ftp server')
    ftp.quit()


def get_the_latest_file_in_a_folder(path):
    list_of_files = os.listdir(path)  # get a list of all file names in a folder
    # get a list of absolute paths for previously recovered files
    paths = [os.path.join(path, basename) for basename in list_of_files]
    # return the latest (most recent modified metadata) file
    return max(paths, key=os.path.getctime)


def get_max_file_name_with_wildcard(file_pattern):
    file = max(glob.glob(file_pattern))
    return file


def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    # returning all file paths
    return file_paths


def zip_files(file_paths_to_zip, directory_log_path, zip_name):
    os.chdir(directory_log_path)
    logging.info('following files will be zipped:')
    for file_name in file_paths_to_zip:
        logging.info(file_name)
    # create timestamped file name
    current_date = time.strftime("%Y%m%d")
    current_time = time.strftime("%H%M%S")
    zip_name = current_date + "_" + current_time + "_" + zip_name + ".zip"
    # writing files to a zipfile
    logging.info('zipping files...')
    with ZipFile(zip_name, mode='w', compression=ZIP_DEFLATED, allowZip64=False) as zip:
        # writing each file one by one
        for file in file_paths_to_zip:
            zip.write(file)
    logging.info('All files zipped successfully !')
    return zip
