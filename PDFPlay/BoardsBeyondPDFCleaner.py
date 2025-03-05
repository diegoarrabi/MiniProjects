from os import path
from os import listdir
from os import remove
from os import mkdir
from os import rename

from time import sleep

from pypdf import PdfWriter
from pypdf import PdfReader


def makeBackup(item_path: str) -> str:
    backup_suffix = "_backup"
    item_basename = f"{path.basename(item_path)}{backup_suffix}"
    backup_path = path.join(item_path, item_basename)
    count = 1
    while path.isdir(backup_path):
        backup_items = listdir(backup_path)
        if len(backup_items) > 0:
            if ".DS_Store" in backup_items and (len(backup_items) == 1):
                remove(path.join(backup_path, ".DS_Store"))
                return backup_path
        item_name = f"{item_basename}_{count}"
        backup_path = path.join(item_path, item_name)
        count += 1
    mkdir(backup_path)
    sleep(1)
    return backup_path

def sortItems(dir_items: list[str]) -> None:
    ds_store = ".DS_Store"
    for item in dir_items:
        file_name = path.basename(item)
        if ds_store in [file_name]:
            remove(item)
            dir_items.remove(item)
    dir_items.sort()

def moveToBackup(current_path: str, new_path: str) -> None:
    item_basename = path.basename(current_path)
    new_full_path = path.join(new_path, item_basename)
    rename(current_path, new_full_path)
    sleep(1)

def actOnPdf(pdf_fullpath: str, pdf_newpath: str) -> None:
    # MAKE NEW PDF NAME
    
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(pdf_fullpath, strict=False)
    moveToBackup(pdf_fullpath, pdf_newpath)
    
    _, _, page_dimensions, _ = pdf_reader.pages[0].mediabox
    number_buffer = len(str(len(pdf_reader.pages)))

    # EACH PAGE
    for page in pdf_reader.pages:
        # print(f"PAGE {count:0>{number_buffer}}")
        # SKIP PAGES THAT ARE NOT OF THE SAME DIMENSION
        _, _, current_page_dimensions, _ = page.mediabox
        if current_page_dimensions != page_dimensions:
            continue
        # REMOVE ANNOTATIONS
        if page.annotations is not None:
            page.annotations.clear()
        page_text = page.extract_text()
        
        added_page = pdf_writer.add_page(page)
        
        
        if "Jason Ryan" in page_text:
            page_text_list = page_text.splitlines()
            subtopic_title = page_text_list[0]
            pdf_writer.add_outline_item(subtopic_title, added_page)
        

    # USES THE SAME FILE NAME; ORIGINALS MOVED INTO BACKUP
    with open(pdf_fullpath, "wb") as output_pdf:
        pdf_writer.write(output_pdf)
    pdf_reader.close()



def main() -> None:
    # pdf_dir_path = "/Users/diegoibarra/Downloads/test"
    pdf_dir_path = "/Users/diegoibarra/Media/Medicine Videos/Clinical/test"
    backup_path = makeBackup(pdf_dir_path)

    pdf_list = listdir(pdf_dir_path)
    pdf_path_list = [path.join(pdf_dir_path, pdf_file) for pdf_file in pdf_list if path.isfile(path.join(pdf_dir_path, pdf_file))]
    sortItems(pdf_path_list)
    
    for pdf_path in pdf_path_list:
        actOnPdf(pdf_path, backup_path)


if __name__ == "__main__":
    main()