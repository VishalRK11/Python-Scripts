__author__ = 'Vishal'

import os
import shutil


def copy_files():
    current_dir = ""  # Enter the path of the directory, from where you want to copy, here.
    destination_dir = ""  # Enter the path of your destination directory.
    extensions = ()  # Enter the extensions of the files you want to copy.

    os.chdir(current_dir)
    for root, _, files in os.walk('.'):
        for file in files:
            if os.path.splitext(file)[1] in extensions:
                src = os.path.join(root, file)
                print("Copying the file %s ..." % file)
                shutil.copy(src, destination_dir)
    print("Finished copying all the files")


if __name__ == '__main__':
    copy_files()
