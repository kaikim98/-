import os
import zipfile
from pathlib import Path
import shutil

def create_zip(flies):
    file_list = []

    for path in Path("images/movies/monsters").iterdir():
        file_list.append("images/movies/monsters/" + path.stem + path.suffix)
    
    print(file_list)
    with zipfile.ZipFile("test_archive.zip", "w") as  archive:
        for file in file_list:
            archive.write(file)

def append_zip(files):
    file_list = []

    for path in Path("images/magazine/monsters").iterdir():
        file_list.append("images/magazine/monsters/" + path.stem + path.suffix)
    
    print(file_list)
    with zipfile.ZipFile("test_archive.zip", "a") as  archive:
        for file in file_list:
            archive.write(file)

if __name__ == "__main__":
    shutil.make_archive("directory_archive", "zip", "images/")
