import zipfile

def read_zip(original_zipfile):
    with zipfile.ZipFile(original_zipfile, "r") as archive:
        print(archive.namelist())

def retrieve_file_info_zip(original_zipfile, target_file):
    with zipfile.ZipFile(original_zipfile, "r") as archive:
        file_info = archive.getinfo(target_file)
        print(file_info)    

def read_file_in_zip(original_zipfile, target_file):
    with zipfile.ZipFile(original_zipfile, "r") as archive:
        with archive.open(target_file)as file:
            print(file.read())

def extract_file(original_zipfile, target_file):
    with zipfile.ZipFile(original_zipfile, "r") as archive:
        archive.extract(target_file)

def extract_all(original_zipfile, target_directory):
    with zipfile.ZipFile(original_zipfile, "r") as archive:
        archive.extractall(target_directory)

if __name__ == "__main__":
    # read_zip("test_archive.zip")
    # retrieve_file_info_zip("test_archive.zip", "images/magazine/monsters/article03.txt")
    # read_file_in_zip("test_archive.zip", "images/magazine/monsters/article03.txt")
    # extract_file("test_archive.zip", "images/magazine/monsters/article03.txt")
    extract_all("target")