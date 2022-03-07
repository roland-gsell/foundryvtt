#!/usr/bin/env python3

import tarfile
import datetime

# Config-Part
# change as needed

data_dir = '/home/roland/foundrydata'
fvtt_dir = '/home/roland/foundryvtt'
excludes = ['gAudioBundle-', 'SoundBoard-BlitzFreePack']


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

print('processing {} ...'.format(data_dir))
out = tarfile.open(data_file, mode='w:gz')
out.add(data_dir, filter=filter)
out.close()
print('written {}.'.format(data_file))

print('processing {} ...'.format(fvtt_dir))
out = tarfile.open(fvtt_file, mode='w:gz')
out.add(fvtt_dir, filter=filter)
out.close()
print('written {}.'.format(fvtt_file))
print('')
