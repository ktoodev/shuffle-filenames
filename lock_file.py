###
# Interact with the shuffle lock file
### 

from os import path
import yaml

###
# Safety: check that the 'permissions' file is there so we don't accidentally randomize folders we don't want to
###
def check_lock (file_path, token):

    # check the lock file exists
    if not path.isfile(file_path):
        return False

    # open lock file
    with open(file_path, "r") as config_file:

        lock_values = yaml.load(config_file, Loader=yaml.FullLoader)

        # check the 'dir' parameter in the lock file (should always point to the same path as the file itself to protect against the file being moved/copied accidentally)
        if 'dir' not in lock_values or path.join (lock_values['dir'], '') != path.join(path.dirname(file_path), ''):
            print ("The \"dir\" name in the lock file is different from the directory we're trying to randomize (expected value: " + path.dirname(file_path) + ")")
            return False

        # check that the token matches one on the lock file
        if 'token' not in lock_values or lock_values['token'] != token:
            print ("The provided token did not match a token found in the lock file")
            return False
        
        return True