#!/usr/bin/env python3

import tarfile
import datetime
from tqdm import tqdm
import os


# Config-Part
# change as needed

data_dir = '/home/roland/foundrydata/'
fvtt_dir = '/home/roland/foundryvtt/'
excludes = ['gAudioBundle-1',
            'gAudioBundle-2',
            'gAudioBundle-3',
            'gAudioBundle-4',
            'SoundBoard-BlitzFreePack',
            ]


# Script-Part
# don't change below unless you know what you are doing

print('creating archives')
today = str(datetime.datetime.now())
filename = today.split('.')[0].replace(':', '-').replace(' ', '_')
data_file = '{}_{}{}'.format('data', filename, '.tar.gz')
fvtt_file = '{}_{}{}'.format('fvtt', filename, '.tar.gz')

def filter(tarinfo):
    for exclude in excludes:
        if exclude in tarinfo.name:
            return None
    return(tarinfo)

def compress(tar_file, folder):
    members = list()
    for root, dirs, files in os.walk(folder):
        for name in files:
            members.append(os.path.join(root, name))
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:gz")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member, recursive=False, filter=filter)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()

print('processing {} ...'.format(data_dir))
compress(data_file, data_dir)
print('written {}.'.format(data_file))
print('')

print('processing {} ...'.format(fvtt_dir))
compress(fvtt_file, fvtt_dir)
print('written {}.'.format(fvtt_file))
print('')
