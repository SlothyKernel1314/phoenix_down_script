import os
import time


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


def create_timestamped_and_named_file(application_name):
    current_date = time.strftime("%Y%m%d")
    current_time = time.strftime("%H%M%S")
    format_file_name = current_date + "_" + current_time + "_" + application_name + "_log_phoenix_down.txt"
    return format_file_name

