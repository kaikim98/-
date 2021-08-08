import os
import zipfile
from pathlib import Path


if __name__ == '__main__':
    print(os.listdir('.'))

    file_list = []

    for path in Path('images/movies/monster').iterdir():
        file_list.append()
    
    #with zipfile.ZipFile('test_archive.zip', 'w') as archive:
    #    for file in os.listdir('.'):
    #        archive.write(file)

def append_zip(files):
    file_list = []

    for path in Path('images/movies/monster').iterdir():
        file_list.append('images/movies/monster/'+path.stem+path.suffix)

    print(file_list)
    with zipfile.ZipFile('test_archive.zip', 'a') as archive:
        for file in file_list:
            archive.write(file)

if 