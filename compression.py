#!/usr/bin/python2.7

# Compress   : Created by Ruslan Tyutin
# Description: The script runs through all files with the specified extension.
#              Archives and deletes the original files, except the last.
#              To work, you must specify the full path and file extension for archiving

import os

FULL_PATH_TO_DIR = '/tmp/call_record'
EXTENSION_FILE = 'pcapng'


def compress(path, mask=''):
    os.chdir(path)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if mask != '':
        match_list = [x for x in files if x.endswith(mask)]
        files = match_list
    for f in sorted(files)[:-1]:
        os.system('tar -cjf %s %s' % (f + '.tar.bz2', f))
        os.system('rm ' + f)


if __name__ == '__main__':
    compress(FULL_PATH_TO_DIR, EXTENSION_FILE)
