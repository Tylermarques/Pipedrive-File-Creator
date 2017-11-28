import docx

with open("../MCA.docx", 'rb') as doc:

    document = docx.Document(doc)
    print(document)
    for i in document.paragraphs:
        print(i.text)