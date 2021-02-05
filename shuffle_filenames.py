###
# Randomize file names in a directory
###

import os
from os import path
import argparse

from lock_file import check_lock
from randomize_files import shuffle_names


# set up parser args
parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="The directory to randomize files in")
parser.add_argument("--token", help="An arbitrary string, corresponding to the token in the lock file to ensure the right directory is being targeted", required=True)
args = parser.parse_args()


# get the directory to randomize files in
if args.dir and path.isdir(args.dir):
    dir_path = args.dir
else:
    dir_path = os.getcwd()


# check the lock file before proceeding 
if not check_lock (dir_path, args.token):
    print ('Failed to validate the lock file (must have a "dir" value matching the directory to randomize and a "token" value matching the one used to call this script)')
else:
    shuffle_names(dir_path)
    print ('Lock file approved')
