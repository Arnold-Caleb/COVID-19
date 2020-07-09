###file system paths and semantics for different operating systems###
import os
from pathlib import Path

# Default folders containing the files to be renamed
TEST, TRAIN, VAL = 'datasets/test', 'datasets/train', 'datasets/val'

'''
Navigate to the directory containing the files that contain files that need to be renamed
from the current working directory
'''
def rename_files(folder_path):
    current_dir = Path.cwd().parent
    split_dir = current_dir.joinpath(folder_path)
    #iterate over the folders that contain the files that need to be renamed

    for folder in split_dir.iterdir():
        for i, f in enumerate(folder.iterdir()):
            b = f.parent
            if f.suffix == '.jpeg': # rename files that have the .jpeg extension
                f = f.rename(b.joinpath('{:04d}'.format(i+1) + '.jpeg'))
            elif f.suffix == '.jpg': # rename files that have .jpg extension
                f = f.rename(b.joinpath('{:04d}'.format(i+1) + '.jpg'))    
            elif f.suffix == '.png': # rename files that have .png extension
                f = f.rename(b.joinpath('{:04d}'.format(i+1) + '.png'))
            else:
                continue

rename_files(TEST)
rename_files(TRAIN)
rename_files(VAL)
