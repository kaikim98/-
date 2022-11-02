import tarfile

def create_tar_archive():
    #images/newspaper/monsters에 있는 파일 tar형식으로 생성
    file_list = []

    for path in Path('images/newspaper/monsters').iterdir():
        file_list.append('images/newspaper/monsters/'+path.stem+path.suffix)
    
    with tarfile.open('monster_archive.tar', 'w') as tar:
        for file in file_list:
            tar.add(file)


def add_to_tar_archive():
    # images/movies/monsters에 있는 파일을 기존 tar 파일에 추가
    with tarfile.open('monster_archive.tar','a') as tar:
        tar.add('images/movies/monsters/monsters_new__new_monster01.png')
        tar.add('images/movies/monsters/monsters_new__new_monster03.png')
        tar.add('images/movies/monsters/monsters_new__new_monster05.png')

def extract_tar():
    # images/moves/monsters/monsters_new__new_monster01.png만 압축해제
    with tarfile.open('monster_archive.tar', 'r') as tar:
        tar.extract('images/moves/monsters/monsters_new__new_monster05.png')

def extract_all():
    # extracted_monster_files에 모든 파일 압축해제
    with tarfile.open('monster_archive.tar', 'r') as tar:
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, "extracted_monster_files")