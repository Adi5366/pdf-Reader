import pdfplumber

# with pdfplumber.open("sample-tables.pdf") as pdf:
#     tables = pdf.pages[0].extract_tables()

#     if tables:
#         for table in tables:
#             print(table)

'''
    Using tabula Library
'''

import tabula

# Read the PDF file
df = tabula.read_pdf("sample-tables.pdf", pages='all')

# If you expect multiple tables and want to concatenate them
#df = tabula.read_pdf("path/to/your/file.pdf", pages='all', multiple_tables=True)

# Display the extracted tables
for table in df:
    print(table)


