from os import path
from os import listdir
from os import remove
from os import rename
from os import get_terminal_size

import time

def clearScreen() -> None:
    print("\x1b[H\x1b[J")

def checkInput(input_value: str) -> str:
    if input_value.lower() in ["q", "quit"] or not path.exists(input_value):
        input_value = input_value.replace("'", "")
        if not path.exists(input_value):
            exit(clearScreen())
    return input_value

def sortTopics(dir_items: list[str], dir_path: str) -> None:
    ds_store = ".DS_Store"
    dir_items.sort()
    if ds_store in dir_items:
        remove(path.join(dir_path, str(ds_store)))
        dir_items = dir_items.remove(ds_store)

def removeSpecialCharacter(item: str) -> str:
    character_list = (" ", "_", "-", ".")
    while item.startswith(character_list):
        item = item[1:]
    return item

def removeNumbers(item: str) -> dict:
    item_number = ""
    item_dict = {"Name": "", "Number": 0}
    item = removeSpecialCharacter(item)
    
    if item[0].isdigit():
        while item[0].isdigit():
            item_number += item[0]
            item = item[1:]
    else:
        item_number = "0"

    item_dict["Name"] = removeSpecialCharacter(item)
    item_dict["Number"] = int(item_number)
    return item_dict

def renameItem(newname: str, oldpath:str) -> None:
    parent_directory = path.dirname(oldpath)
    rename(oldpath, path.join(parent_directory, newname))

def main():
    separator = ". "
    paths_edited = []
    while True:
        add_to_list = True
        terminal_width,_ = get_terminal_size()
        clearScreen()
        for item in paths_edited:
            print(f"{item:>{terminal_width}}")
        print("-"*(terminal_width-1))

        # MAIN DIRECTORY PATH
        input_directory = checkInput(input("PATH \n: "))
        # input_directory = "/Users/diegoibarra/Media/Clinical/Test"
        
        main_directory_name_list = listdir(input_directory)
        sortTopics(main_directory_name_list, input_directory)
        
        for subdir_name in main_directory_name_list:
           
            # SUBDIRECTORY PATH
            subdir_path = path.join(input_directory, subdir_name)

            if not path.isdir(subdir_path) or subdir_name.startswith("."):
                break
            subdir_contents_name_list = listdir(subdir_path)
            sortTopics(subdir_contents_name_list, subdir_path)

            count = 0
            
            pad_count = len(str(len(subdir_contents_name_list)))
            if pad_count == 1:
                pad_count = 2
            for content_name in subdir_contents_name_list:
                
                
                # CONTENT PATH
                content_path = path.join(subdir_path, content_name)
        
                path_basename = path.basename(subdir_path)                
                new_name_dict = removeNumbers(content_name)
                
                if new_name_dict["Number"] == 0:
                    new_name_dict["Number"] = count
                    count += 1

                new_name = f"{new_name_dict["Number"]:0>{pad_count}}{separator}{new_name_dict["Name"]}"
            
                renameItem(new_name, content_path)

        if add_to_list:
            paths_edited.append(path_basename)

if __name__ == "__main__":
    main()


