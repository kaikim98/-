from datetime import datetime
import os

def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formated_date

# 내가 지정한 디렉토리에 무슨 파일이 있는지 확인하고 싶다!
# 좀더 개선해서 언제 생성이 되었는지 확인하고 싶다.
def display_entries_in_directory(directory):
    # os.listdir() : 현재 내가 위치한 디렉토리에 존재하는 디렉토리 및 파일을 리스트해서 출력
    with os.scandir() as entries:
        for entry in entries:
            print("이름 : ", entry.name)
            info = entry.stat()
            print("생성 시간 : ", format_datetime(info.st_ctime))
            # print("생성 시간 : ", info.st_birthtime) 맥이나 리눅스의 경우
            print("최종 수정시간 : ", format_datetime(info.st_atime))
            print("파일의 크기 : ", info.st_size)

            format_datetime(info.st_ctime)


# 나는 디렉토리만 보고 싶다!
def display_directories(directory):
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_dir():
                print("디렉토리 이름 : ", entry.name)

# 나는 파일만 보고 싶다!
def display_files(directory):
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_file():
                print("파일 이름 : ", entry.name)

if __name__ == "__main__":
    display_entries_in_directory("./")
    # display_directories("./")
    # display_files("./")