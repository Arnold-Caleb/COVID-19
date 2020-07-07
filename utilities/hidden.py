###file system paths and semantics for different operating systems###
import os
from pathlib import Path

'''
Navigate to the directory containing the files that contain files that need to be renamed
from the current working directory
'''
current_dir = Path.cwd().joinpath('files')

#iterate over the folders that contain the files that need to be renamed

for folder in current_dir.iterdir():
    for i, f in enumerate(folder.iterdir()):
        b = f.parent
        if f.suffix == '.jpeg': # rename only files that have the .txt extension
            f = f.rename(b.joinpath('{:04d}'.format(i) + '.jpeg'))

