from os import listdir
from os.path import isfile, join
import regex as re


def process_paragraph(paragraph):
    par_text = ''

    for line in paragraph:
        par_text += " " + process_line(line)

    par_text = par_text.strip()

    return par_text


def process_line(sentence):
    proc_snt = re.sub("^\s*|\x0c|", "", sentence)
    proc_snt = re.sub("\.\n", ".", proc_snt)
    proc_snt = re.sub(":\n", ":", proc_snt)
    proc_snt = re.sub(";\n", ";", proc_snt)
    proc_snt = re.sub("^\s*", "", proc_snt)
    proc_snt = re.sub("\n", " ", proc_snt)
    proc_snt = re.sub("[\.]{2,}", "", proc_snt)
    proc_snt = re.sub("[_]{2,}", "", proc_snt)
    proc_snt = proc_snt.strip()

    return proc_snt


text_path = './text/'
onlyfiles = [f for f in listdir(text_path) if isfile(join(text_path, f))]

text_files = [text_path + f for f in onlyfiles if f.split('.')[1] == 'txt']

for file in text_files:
    with open(file) as f:
        lines = f.readlines()

    paragraphs = []
    paragraph = []

    for line in lines:
        if line == '\n':
            if len(paragraph) > 1:
                paragraphs.append(process_paragraph(paragraph))
            paragraph = []
        else:
            paragraph.append(line)

    for par in paragraphs:
        sentences = re.split(r"\.|:|;", par)

        for snt in sentences:
            if len(snt.split()) > 4:
                with open('all_docs_line_by_line.txt', 'a') as f:
                    f.write(snt.strip() + '\n')
