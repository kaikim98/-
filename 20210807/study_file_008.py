import os
from pathlib import Path
import shutil

def rename_os(original_name, changed_name):
    os.rename(original_name, changed_name)

def rename_pathlib(original_name, changed_name):
    file = Path(original_name)
    file.rename(changed_name)

def move_files(original_location, target_location):
    shutil.move(original_location, target_location)

def move_file(original_file, target_location):
    os.mkdir(target_location)
    shutil.move(original_file, target_location)

if __name__ == '__main__':
    # rename_os('articles/article01.txt', 'articles/article_01.txt')
    # rename_pathlib('articles/article02.txt', 'articles/article_02.txt')
    # move_files('text_data/', 'articles/')
    # move_file('articvles/num_series.txt', 'data_number')