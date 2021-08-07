import shutil

def copy_file(original_file, target_location):
    shutil.copy(original_file, target_location)

def copy_file_with_metadata(original_file, target_location): #파일의 메타정보까지 복사
    shutil.copy2(original_file, target_location)

def copy_directory(original_location, target_location):
    shutil.copytree(original_location, target_location) # shutil.copy는 밑에 파일들까지 통쨰로 복사는 안됨

if __name__ == '__main__':
    # copy_file('articles/article_01.txt', 'data_article')
    # copy_file_with_metadata('articles/article_01.txt', 'data_article')
    # copy_directory('articles/', 'backup_articles/')