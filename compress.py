#!/usr/bin/python3.6

# Compress   : Created by Ruslan Tyutin
# Description: The script runs through all files with the specified extension.
#              Archives and deletes the original files, except the last.
#              To work, you must specify the full path and file extension for archiving

import os
import shutil
from datetime import datetime

COUNT_ZIP_FILES = 2
SOURCE_DIR = os.getcwd() + '/test_dir'
DESTINATION_DIR = os.getcwd()


def get_zip_files():
    return [name for name in os.listdir(DESTINATION_DIR) if os.path.isfile(name) and name.endswith(".zip")]


def get_name_from_date():
    d = datetime.now()
    return 'backup_' + d.strftime('%Y%m%d')


def get_the_last_old_file():
    files = get_zip_files()
    last_old_file = files[0]

    if not last_old_file:
        return none

    for file in files:
        if os.path.getctime(file) < os.path.getctime(last_old_file):
            last_old_file = file

    return last_old_file


if __name__ == '__main__':
    shutil.make_archive(get_name_from_date(), 'zip', SOURCE_DIR)
    while len(get_zip_files()) > COUNT_ZIP_FILES:
        os.remove(get_the_last_old_file())
