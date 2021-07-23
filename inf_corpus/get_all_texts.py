from os import listdir
from os.path import isfile, join

text_path = './text/'
onlyfiles = [f for f in listdir(text_path) if isfile(join(text_path, f))]

text_files = [text_path + f for f in onlyfiles if f.split('.')[1] == 'txt']

all_lines = []
for file in text_files:
    with open(file) as f:
        lines = f.readlines()

    all_lines += lines

with open('all_docs.txt', 'w') as f:
    f.writelines(all_lines)
