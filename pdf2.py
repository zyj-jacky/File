"""
读取PDF文件
"""

from PyPDF2 import PdfFileReader

with open('张跃杰-17797756555-应聘Python开发类职位', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(5)
    print(current_page)
    print(current_page.extractText())
