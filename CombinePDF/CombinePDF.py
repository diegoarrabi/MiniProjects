#!/Users/diegoibarra/.config/pyenv/versions/3.13.0/envs/CombinePDF/bin/python

from pypdf import PdfReader
from pypdf import PdfWriter
from pypdf import PdfMerger
from pypdf.annotations import FreeText

from os import path
from os import mkdir
from os import listdir

## GLOBAL VARIABLES
temp_dir_name = "temp"

## FUNCTIONS
def clearScrean() -> None:
    print("\x1b[H\x1b[J")

def userError() -> None:
    exit(print("K."))

def inputSetup(user_input: str) -> list[str]:
    global temp_dir_name

    pdf_list = []
    if user_input.lower() == "done":
        userError()
    while True:
        if not path.exists(user_input):
            print("Path provided does NOT exist")
            userError()
        elif path.isfile(user_input):
            print("Path provided is a File, NOT a Directory")
            userError()

        dir_contents = listdir(user_input)
        
        for item in dir_contents:
            if item.endswith(('.pdf', '.PDF', '.Pdf')):
                item_path = path.join(user_input, item)
                pdf_list.append(item_path)
            else:
                pass
        if len(pdf_list) == 0:
            print("No PDFs found in Directory")
            userError()
        else:
            count = 1
            while True:
                if path.isdir(path.join(user_input, temp_dir_name)):
                    prefix = "_" * count
                    temp_dir_name = f"{prefix}{temp_dir_name}"
                else:
                    # MAKE TEMPORARAY DIRECTORY
                    mkdir(path.join(user_input, temp_dir_name))
                    break
            break
    return pdf_list

def addPageNumber(pdf: str) -> str:
    global temp_dir_name
    dir_name = path.dirname(pdf)
    pdf_name = path.basename(pdf)[:-4]
    output_name = path.join(dir_name, temp_dir_name, f"{pdf_name}-{temp_dir_name}.pdf")
    # print(output_name)

    reader = PdfReader(pdf)
    page_obj = reader.pages[0]
    writer = PdfWriter()
    writer.add_page(page_obj)
    
    pdf_name_annotation = FreeText(
        text=pdf_name,
        rect=(0, 750, 50, 800),
        font="Arial",
        font_size="20pt",
        font_color="000000",
        )
    pdf_name_annotation.flags = 4

    writer.add_annotation(page_number=0, annotation=pdf_name_annotation)
    # with open(output_name, "wb") as pdf_edit:
        # writer.write(pdf_edit)
    
    return output_name

def mergeNewPages(pdf:str) -> None:
    global temp_dir_name

    print()

def main():
    clearScrean()
    # pdf_directory = input("Enter Full Path of Directory Containing PDFs (or 'done' to exit)\n: ")
    pdf_directory = "/Users/diegoibarra/Developer/1_myProjects/Misc/Slices"
    pdf_list = inputSetup(pdf_directory)
    pdf_list.sort()

    temp_marked_pdf = []
    for pdf in pdf_list:
        temp_marked_pdf.append(addPageNumber(pdf))

    for pdf in temp_marked_pdf:
        # pdf_name = path.basename(pdf)[:-4]
        # print(path.dirname(pdf))
        print(pdf)


if __name__ == "__main__":
    main()




