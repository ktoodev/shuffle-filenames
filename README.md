# shuffle_filenames

Simple script to randomize the names of files in a directory (by randomly swapping with other filenames in the folder).

| :warning: **Warning: while there's a "lock file" to try and make sure the program is run intentionally, this system is not foolproof - please read all the documentation and use the script with care! Randomly shuffling filenames is usually very bad!** |
| --- |

## Usage

The script uses a special file called `_shuffle-lock` to guard against unintended invocation. The file must be in the directory where you want to shuffle filenames and must have two parameters in it, `token` and `dir`:
- `token` is an arbitrary string that must be the same in the `__shuffle-lock` file and the command line argument
- `dir` must be the directory you want to shuffle (and where the `_shuffle-lock` is located)

The script takes two corresponding command line arguments (`token` and `dir`), which must match the values in the `_shuffle_lock` file.

### Example `_shuffle-lock` file

    dir: C:\path\to\folder\to\randomize
    token: token_value


### Caveats and warnings

- The script currently skips files that end in ".exe" or start with a "." or "_"
- **The script is not currently designed to work with folders containing a mix of file types.** It **will** currently swap files without regard to their extensions, so if there are multiple file types you'll probably end up with some files that don't work anymore. 


## Calling the script

### In Python:

    python shuffle_filenames.py --token token_value --dir C:\path\to\folder\to\randomize

### Executable package ([downloadable from releases](https://github.com/ktoodev/shuffle-filenames/releases)):

    shuffle_filenames --token token_value --dir C:\path\to\folder\to\randomize


## Build

To build an executable with PyInstaller:
    # install pyinstaller if it isn't already installed
    https://github.com/ktoodev/shuffle-filenames

    # run pyinstaller 
    python -m PyInstaller --onefile 'shuffle_filenames.py'