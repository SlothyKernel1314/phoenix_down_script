from credentials import *
from constants import *
import os
import time
from ftplib import FTP
from zipfile import ZipFile


def create_directory(path):
    # If the work directory doesn't existe yet...
    # ... creation of this directory
    if not os.path.isdir(path):
        os.makedirs(path)
        print("The folder " + path + " was successfully created")
    else:
        print("The folder " + path + " already exists")

    # Designation of the working directory as current directory
    os.chdir(path)


def create_timestamped_directory():
    current_date = time.strftime("%Y%m%d")
    current_time = time.strftime("%H%M%S")
    format_directory_name = current_date + "_" + current_time
    os.mkdir(format_directory_name)
    return format_directory_name


def create_timestamped_and_named_file(application_name):
    current_date = time.strftime("%Y%m%d")
    current_time = time.strftime("%H%M%S")
    format_file_name = current_date + "_" + current_time + "_" + application_name + "_log_phoenix_down.txt"
    return format_file_name


def upload_file_to_server_ftp(file, filename, application_name):
    ftp = FTP(SEEDBOX_DOMAIN_NAME)  # connect to host, default port
    ftp.login(user=SEEDBOX_USER_NAME, passwd=SEEDBOX_PASSWD)  # login with credentials
    # TODO: gérer une exception en cas de log impossible
    ftp.retrlines('LIST')  # LIST retrieves a list of files and information about those files
    ftp.cwd(SEEDBOX_ROOT_PD_SCRIPT_PATH + "/" + application_name)  # Set the current directory on the server
    ftp.storbinary('STOR ' + filename + '', file)  # uploading file to the server
    ftp.quit()


def get_the_latest_file_in_a_folder(path):
    list_of_files = os.listdir(path) # get a list of all file names in a folder
    # get a list of absolute paths for previously recovered files
    paths = [os.path.join(path, basename) for basename in list_of_files]
    # return the latest (most recent modified metadata) file
    return max(paths, key=os.path.getctime)


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
