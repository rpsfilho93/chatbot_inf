from haystack.nodes import PDFToTextConverter

from haystack.nodes import PreProcessor

from haystack.document_stores import ElasticsearchDocumentStore

from os import listdir
from os.path import isfile, join

dir_path_pdf = './inf_corpus/pdf'
files = [f for f in listdir(dir_path_pdf) if isfile(join(dir_path_pdf, f))]
pdf_files = [file for file in files if file.split('.')[1] == 'pdf']

converter = PDFToTextConverter(
    remove_numeric_tables=True, valid_languages=['pt'])

preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=True,
    split_by="word",
    split_length=100,
    split_respect_sentence_boundary=False
)

docs = []
for pdf in pdf_files:
    doc_pdf = converter.convert(file_path=join(dir_path_pdf, pdf), meta={
                                'name': pdf.split('.')[0]}, encoding='UTF-8')

    with open('./inf_corpus/preprocessed/docs/' + pdf.split('.')[0] + '.txt', 'w') as f:
        f.write(doc_pdf[0]['content'])

    doc_splits = preprocessor.process(doc_pdf)
    docs = docs + doc_splits

for doc in docs:
    with open('./inf_corpus/preprocessed/splits/' + doc['meta']['name'] + '-split-' + str(doc['meta']['_split_id']) + '.txt', 'w') as f:
        f.write(doc['content'])

document_store = ElasticsearchDocumentStore()
document_store.delete_documents()
document_store.write_documents(docs)

print(f"n_files_input: {len(pdf_files)}\nn_docs_output: {len(docs)}")
