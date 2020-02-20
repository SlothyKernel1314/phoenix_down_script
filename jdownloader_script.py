from utilities import *
import shutil


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
    dlzip_file = get_max_file_name_with_wildcard("downloadList*.zip")

    # add downloadList*.zip file to files list to backup
    files_list_to_backup.append(dlzip_file)

    # get latest linkcollector*.zip file
    lnkcoll_file = get_max_file_name_with_wildcard("linkcollector*.zip")

    # add linkcollector*.zip file to files list to backup
    files_list_to_backup.append(lnkcoll_file)

    # get the path of log directory
    directory_log_path = PD_SCRIPT_ROOT_PATH + "/" + application_name + "/" + str(timestamped_directory)

    # copying local files (in order to backup) to phoenix down script firefox directory
    for file in files_list_to_backup:
        shutil.copy(file, directory_log_path)

    # get all files paths in log (timestamped) diectory in order to zip theses files + server upload
    file_paths_to_zip = get_all_file_paths(directory_log_path)

    # zip all files
    zip_file = zip_files(file_paths_to_zip, directory_log_path, JDOWNLOADER_ZIP_FILE_BASENAME)

    # opens the zip file for reading only in binary format in order to upload
    opened_zip_file = open(zip_file.filename, "rb")

    # upload zip to ftp server
    upload_file_to_server_ftp(opened_zip_file, zip_file.filename, application_name)

    # delete local zip file
    os.remove(zip_file.filename)






