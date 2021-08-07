import os
import zipfile
from pathlib import Path


if __name__ == '__main__':
    print(os.listdir('.'))
    for path in Path('images/movies/monster').iterdir():
        print(type(path))
    
    #with zipfile.ZipFile('test_archive.zip', 'w') as archive:
    #    for file in os.listdir('.'):
    #        archive.write(file)