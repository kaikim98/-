from pathlib import Path


if __name__ == '__main__':
    entries = Path.cwd()
    # entries = Path.home()
    # entries = Path('images')
    
    for entry in  entries.iterdir():
        print(entry.name)
        print(entry.parent)
        print(entry.parent.parent)
        print(entry.stem)
        print(entry.suffix) # 확장명
        print(entry.stat())
        print('========================')