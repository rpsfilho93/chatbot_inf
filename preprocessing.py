from haystack.file_converter.pdf import PDFToTextConverter

from haystack.preprocessor.utils import convert_files_to_dicts, fetch_archive_from_http
from haystack.preprocessor.preprocessor import PreProcessor

from haystack.document_store import ElasticsearchDocumentStore

from os import listdir
from os.path import isfile, join

dir_path = './inf_corpus/pdf'
files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
pdf_files = [file for file in files if file.split('.')[1] == 'pdf']

converter = PDFToTextConverter(
    remove_numeric_tables=True, valid_languages=['pt'])

docs = []
for pdf in pdf_files:
    doc_pdf = converter.convert(file_path=join(dir_path, pdf), meta={
                                'name': pdf.split('.')[0]}, encoding='UTF-8')
    doc_name = doc_pdf['meta']['name'] + ' [SEP] '

    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=False,
        split_by="word",
        split_length=100 - len(doc_name),
        split_respect_sentence_boundary=False
    )

    doc_splits = preprocessor.process(doc_pdf)

    for doc_split in doc_splits:
        doc_split['text'] = doc_name + doc_split['text']
        docs.append(doc_split)


document_store = ElasticsearchDocumentStore()
document_store.delete_documents()
document_store.write_documents(docs)
