###
# Randomize filenames
###

import os
import random

###
# Do the randomization
###
def shuffle_names (dir):

    # validate that the directory exists
    if not os.path.isdir(dir):
        return False


    # build a list of all the filenames in the directory
    all_filenames = []

    for entry in os.scandir(dir):
        if not entry.is_file() or entry.path.endswith('.exe') or entry.name.startswith('_') or entry.name.startswith('.'):
            continue
        
        all_filenames.append(entry.name)

    # randomize the order of the array 
    random.shuffle(all_filenames)

    # go through all the files again to rename them
    renamed_count = 0
    for file in all_filenames:

        # create a list of all the files that are NOT this one, so we don't try to swap a file with itself
        other_filenames = list (all_filenames)
        other_filenames.remove(file)

        old_name = os.path.join (dir, file)
        new_name = os.path.join(dir, random.choice (other_filenames))
        temp_name = os.path.join(dir, file + '- ' + str (random.randint(100000, 99999999)) + '.temp')

        # give the new filename a temporary name to avoid collisions
        os.rename(new_name, temp_name)

        # raname from the old name to the new one
        os.rename(old_name, new_name)

        # give the file that WAS the new one (now temp) the old file's name (completing the swap)
        os.rename(temp_name, old_name)

        renamed_count = renamed_count + 1

    print ("Renamed " + str(renamed_count) + " files")