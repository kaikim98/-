from datetime import datetime

import os

def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime('%d %b %Y %H %M %S')
    return formated_date
    
#내가 지정한 디렉토리에 무슨 파일이 있는지 확인하고 싶다!
# 좀더 개선해서 언제 생성이 되었는지 확인하고 싶다
def display_entries_in_directory(directory):
    with os.scandir() as entries:
        for entry in entries:
            print('이름 :', entry.name)
            info = entry.stat()
            print('생성시간 : ', format_datetime(info.st_ctime))
            print('최종 수정시간: ', format_datetime(info.st_atime))
            print('파일의 크기: ', info.st_size)

# 나는 디렉토리만 보고 싶다
def display_directories(directory):
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_dir():
                print('디렉도리 이름 : ', entry.name)

# 나는 파일만 보고싶다
def display_files(directory):
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_file():
                print('파일 이름: ', entry.name)

if __name__ == '__main__':
    display_entries_in_directory("./")
    #display_directories('./')
    #display_files('./')