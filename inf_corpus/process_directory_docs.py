from os import listdir, register_at_fork
from os.path import isfile, join
import regex as re
import json
import sys


def main():
    process_directory_docs(sys.argv[1], sys.argv[2])


def process_directory_docs(input_path, output_path):
    print('Looking for text documents at ', input_path)
    files = [f for f in listdir(input_path)
             if isfile(join(input_path, f))]
    text_files = [file for file in files if file.split('.')[1] == 'txt']

    print('\n...\n')
    print('List of found files:')
    for file_name in text_files:
        print(file_name)

    for file in text_files:
        with open(input_path + '/' + file) as f:
            lines = f.readlines()

        paragraphs = []
        paragraph = []

        for line in lines:
            if line == '\n':
                if len(paragraph) > 3:
                    paragraphs.append(process_paragraph(paragraph))
                    paragraph = []
            else:
                paragraph.append(line)

        file_name = file.split('.')[0]
        json_data = {"title": file_name, "paragraphs": paragraphs}

        with open(output_path + '/' + file_name + '.json', 'w') as output_file:
            json.dump(json_data, output_file)
            output_file.close()


def process_paragraph(paragraph):
    par_text = ''

    for line in paragraph:
        par_text += process_sentence(line)

    par_text = par_text.strip()

    return par_text


def process_sentence(sentence):
    proc_snt = re.sub("^\s* | \x0c | ", "", sentence)
    proc_snt = re.sub("\.\n", ".", proc_snt)
    proc_snt = re.sub(":\n", ":", proc_snt)
    proc_snt = re.sub(";\n", ";", proc_snt)
    proc_snt = re.sub("^\s*", "", proc_snt)
    proc_snt = re.sub("\n", " ", proc_snt)
    proc_snt = re.sub("[\.]{2,}", "", proc_snt)

    return proc_snt


if __name__ == "__main__":
    main()
