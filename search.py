import os

print("Please enter the text you are looking for")
substr=str(input()).lower()
print("Please enter the dir to search")
base_dir = str(input())
print("\n","*"*10, "substring: ",substr, "*"*10)

def find_text(file):
    with open(file, encoding="utf8", errors="ignore") as fp:
        lines = [line.lower() for line in fp.readlines()]
        match = [(i+1,line) for i, line in enumerate(lines) if substr in line]
        if len(match)>0:
            print('\n\n', '*'*60,'\n\nFile name: ', file, '\n', 'Match at line: ', match[0][0], '\n', sep='')
            for i,txt in enumerate(lines):
                print(i+1,'.', txt, end='')

def find_files(root):
    tup = next(os.walk(root))
    files = tup[2]
    folders = tup[1]
    for file in files:
        filename=os.path.join(root, file)
        if filename.endswith('.sql') or filename.endswith('.txt'):
            find_text(filename)
    for folder in folders:
        find_files(os.path.join(root, folder))
    return -1
    
find_files(base_dir)