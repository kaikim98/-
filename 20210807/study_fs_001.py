import os

# 현재 내가 위치한 디렉토리 경로 알고싶다
def display_cwd(): # current working directory
    cwd = os.getcwd()
    print('현재 위치한 디렉토리는 :', cwd)

# 내가 위치한 현재 디렉토리의 상위로 이동하고 싶다
# chdir : change directory / 운영체제에서 ..의 의미는 상위 디렉토리 / .의 의미는 현재 디렉토리
# 리눅스나 맥의 경우 ~의 의미는 사용자의 홈 디렉토리 의미
def up_one_directory_level():
    os.chdir("../") #chdir : change directory 

# 내가 지정한 디렉토리에 무슨 파일이 있는지 확인하고 싶다
def dislay_entries_in_directory():
    # os.listdir() : 현재 내가 위치한 디렉토리에 존재하는 모든 디렉토리를 리스트해서 출력
    # print(os.listdir())
    with os.scandir() as entries:
        for entry in entries:
            print(entry.name)
    
if __name__ == '__main__': #__ : double under(dunder), entry point of python
    display_cwd()
    up_one_directory_level()
    display_cwd()
