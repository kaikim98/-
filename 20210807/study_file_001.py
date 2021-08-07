def write_new_content():
    # with open('descriptions/description-01.txt','w') as f:
    with open('descriptions/description-03.txt','a', encoding = 'UTF-8') as f:
        f.write('안녕하세요!\n')

def print_content():
    with open('descriptions/description-03.txt','r', encoding = 'UTF-8') as f:
        contents = f.read()
        print(contents)

if __name__ == '__main__':
    write_new_content()
    print_content()