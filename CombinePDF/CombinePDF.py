#!/Users/diegoibarra/.config/pyenv/versions/3.13.0/envs/CombinePDF/bin/python

from pypdf import PdfReader
from pypdf import PdfWriter
from pypdf import PdfMerger
from pypdf.annotations import FreeText

from os import path
from os import mkdir
from os import listdir
import os

## GLOBAL VARIABLES
temp_dir_name = ".temp"
temp_dir_path = ""

## FUNCTIONS
def clearScrean() -> None:
    print("\x1b[H\x1b[J")

def userError() -> None:
    exit(print("K."))

def inputSetup(user_input: str) -> list[str]:
    global temp_dir_name
    global temp_dir_path

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
                    temp_dir_path = path.join(user_input, temp_dir_name)
                    mkdir(temp_dir_path)
                    break
            break
    return pdf_list

def deletePDFs():
    pass


def addPageNumber(pdf: str) -> str:
    global temp_dir_name
    global temp_dir_path

    # dir_name = path.dirname(pdf)
    pdf_name = path.basename(pdf)[:-4]
    output_name = path.join(temp_dir_path, f"{pdf_name}.pdf")
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
    with open(output_name, "wb") as pdf_edit:
        writer.write(pdf_edit)
    
    return output_name


def main():
    clearScrean()
    
    pdf_directory = input("Enter Full Path of Directory Containing PDFs (or 'done' to exit)\n: ")
    clearScrean()
    pdf_delete_option = input("Would you like to DELETE the originals? (y/n)\n: ").lower()
    clearScrean()

    # GET PDFS FROM PROVIDED DIRECTORY
    pdf_list = inputSetup(pdf_directory)
    pdf_list.sort()

    # WATERMARK EACH PAGE
    temp_marked_pdf_list = []
    for pdf in pdf_list:
        temp_marked_pdf_list.append(addPageNumber(pdf))

    # COMBINE PDFS
    merger = PdfWriter()
    for pdf in temp_marked_pdf_list:
        merger.append(pdf)
        
    new_file_name = path.join(path.dirname(pdf_directory), f"{path.basename(pdf_directory)}_Merged.pdf")
    merger.write(new_file_name)
    merger.close()

    # REMOVE TEMPORARY DIRECTORY
    all_temp_files_list = listdir(temp_dir_path)
    for pdf in all_temp_files_list:
        temp_pdf_path = path.join(temp_dir_path, pdf)
        os.remove(temp_pdf_path)
    os.rmdir(temp_dir_path)

    # REMOVE ORIGINALS IF OPTED
    if pdf_delete_option == "y":
        for pdf in pdf_list:
            pdf_path = path.join(pdf_directory, pdf)
            os.remove(pdf_path)
        pdf_directory_contents = listdir(pdf_directory)
        if len(pdf_directory_contents) == 0 or (len(pdf_directory_contents) == 1 and pdf_directory_contents[0].lower() == ".ds_store"):
            os.remove(path.join(pdf_directory, ".DS_store"))
            os.rmdir(pdf_directory)
    
    exit(print("DONE (:"))
    
    
        
    


if __name__ == "__main__":
    main()




