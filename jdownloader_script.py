from utilities import *


# VARIABLES ------------------------------------------------------------------------------------------------------------

application_name = "jdownloader"
files_list_to_backup = []


# SCRIPT ---------------------------------------------------------------------------------------------------------------

def jdownloader_script():
    # If the work directory "../jdownloader" doesn't existe yet...
    # ... creation of this directory
    create_directory(PD_SCRIPT_ROOT_PATH + "/" + application_name)

    # creation of timestamped directory
    timestamped_directory = create_timestamped_directory()

    # designation of jdownloader cfg directory as current directory
    os.chdir(JDOWNLOADER_CFG_DIRECTORY_PATH)

    # get latest downloadList*.zip file
    download_list_file = get_max_file_name_with_wildcard("downloadList*.zip")

    # add downloadList*.zip file to files list to backup
    files_list_to_backup.append(download_list_file)



