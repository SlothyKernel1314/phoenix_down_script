import os


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
