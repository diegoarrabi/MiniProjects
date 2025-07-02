import os

from pypdf import PdfReader


def filterInput(_input: str) -> str:
    if _input.startswith(("'", '"')):
        _input = _input.replace("'", "")
        _input = _input.replace('"', '')
    if "\\" in _input:
        _input = _input.replace("\\", "")
    if _input in ['q', 'quit', 'exit', '', ' ']:
        exit()
    return _input


print("\x1b[2J\x1b[H")
file_path = filterInput(input("PDF File Path: \n"))
print("\x1b[2J\x1b[H")

reader = PdfReader(file_path)
pdf_object = reader.pages
# for _page in pdf_object:
#     _text = _page.extract_text()
    
#     print(_text)

print(reader.pages[0].extract_text(space_width=0.000000000001))


reader.close()
