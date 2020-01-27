from constants import *
import os


def create_directory(path):
    # If the work directory doesn't existe yet...
    # ... creation of this directory
    if not os.path.isdir(path):
        os.makedirs(path)

    # Designation of the working directory as current directory
    os.chdir(path)
