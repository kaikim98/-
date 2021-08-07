# 각 문서에서 어떤 문구가 많이 나오는가
import glob

if __name__ == '__main__':
    txt_files = glob.glob('articles/*.txt')
    tracker = dict()
    # print(f'Txt파일 갯수는 {len(txt_files)}')
    for txt in txt_files:
        with open(txt, encoding='UTF-8') as f:
            line = f.readline()
            while line != "":
                words = line.split()
                for word in words:
                    word = word.replace(',', '').replace('.', '').lower()
                    if word not in tracker:
                        tracker[word] = 1
                    else:
                        tracker[word] = tracker[word] +1 
                line = f.readline()

    maxKey = max(tracker, key = tracker.get)
    maxValue = max(tracker.values())

    print(f'가장 많이 등장하는 단어는 {maxKey}')
    print(f'그럼 몇번 나왔을까 {maxValue}')
    print(f'Article 단어사진 : {tracker}')