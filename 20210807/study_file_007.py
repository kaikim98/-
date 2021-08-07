def write_content():
    with open('articles/num-series.txt', 'w') as writer:
        for x in range(50):
            content = f'{x}\n'
            writer.write(content)
        #=> 주의하지 않으면 덮어쓰기가 되어버림

def append_content():
    with open("articles/num-series.txt", "a") as writer:
        for x in range(50, 100):
            content = f"{x}\n"
            writer.write(content)       

if __name__ == '__main__':
