from os import path
from os import listdir
from os import remove
from os import mkdir
from os import rename

from time import sleep

from pypdf import PdfWriter
from pypdf import PdfReader


pdf_file = "Essential Surgery.pdf"
table_of_contents_file = "table_of_contents.txt"


with open(table_of_contents_file, "r") as toc_open_file:
    toc_list = toc_open_file.readlines()

for i in toc_list:
    print(i.replace(".", ". "), end="")
print()


# reader = PdfReader(pdf_file)

# for page in reader.pages:
#     page_text_list = page.extract_text().splitlines()
#     for i in range(0, 3):
#         if page_text_list[i].isdigit():
#             print(page_text_list[i])
#             print(page_text_list[i+1])
#             print(page_text_list[i+2])
#             print(page_text_list[i+3])
#             print(page_text_list[i+4])
#             print()


# reader.close()
