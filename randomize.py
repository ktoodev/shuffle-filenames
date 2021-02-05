###
# Randomize file names in a directory
###

import os
from os import path
import argparse


lock_file_name = '_shuffle-lock'

# Safety: check that the 'permissions' file is there so we don't accidentally randomize folders we don't want to
def check_lock_file (file_path):
    if not path.isfile(file_path):
        return False

    return True


parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="The directory to randomize files in")
args = parser.parse_args()

# get the directory to randomize files in
if args.dir and path.isdir(args.dir):
    dir_path = args.dir
else:
    dir_path = os.getcwd()


lock_file = os.path.join(dir_path, lock_file_name)

if not check_lock_file (lock_file):
    print ('A properly-formatted lock file was not found')