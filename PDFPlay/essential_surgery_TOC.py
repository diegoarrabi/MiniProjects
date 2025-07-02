from os import path
from os import listdir
from os import remove
from os import mkdir
from os import rename

from time import sleep

from pypdf import PdfWriter
from pypdf import PdfReader


pdf_file = "Essential Surgery CH.pdf"

reader = PdfReader(pdf_file)

PAGE_COUNT = 0


# print("\x1b[H", "\x1b[2J")
for page in reader.pages:
    page_text = page.extract_text().splitlines()
    if "CHAPTER OUTLINE" in page_text:
        # str_index = page_text.index("CHAPTER OUTLINE")
        # print(page_text[str_index + 1])
        print(page_text)


reader.close()
