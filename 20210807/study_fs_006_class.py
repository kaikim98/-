import os
from pathlib import Path

def make_logs_dir():
    try:
        os.mkdir("logs/") # mkdir : make directory => 지정한 이름의 디렉토리를 생성
    except FileExistsError as ex:
        print("이미 log 디렉토리가 존재합니다!")


def make_output_dir():
    dir_path = Path("output/")
    dir_path.mkdir(exist_ok=False)

if __name__ == "__main__":
    # make_logs_dir()
    make_output_dir()