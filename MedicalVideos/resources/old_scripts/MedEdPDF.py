from os import path
from os import listdir
from os import remove
from os import mkdir
from os import rename

from time import sleep

from pypdf import PdfWriter
from pypdf import PdfReader


class MiniTopic:
    def __init__(self, name: str, page: str):
        self.name = name
        self.page = page


class SubTopic:
    def __init__(self, name: str, page: str):
        self.name = name
        self.page = page
        self.minitopics = {}

    def addMiniTopic(self, minitopic_object: MiniTopic):
        self.minitopics[minitopic_object.name] = minitopic_object


class MainTopic:
    def __init__(self, name: str, page: int, endpage: int):
        self.name = name
        self.page = page
        self.endpage = endpage
        self.subtopics = {}

    def addSubtopic(self, subtopic_object: SubTopic):
        self.subtopics[subtopic_object.name] = subtopic_object

    def addEndpage(self, endpage: int):
        self.endpage = endpage


def sortItems(dir_items: list[str]) -> None:
    ds_store = ".DS_Store"
    for item in dir_items:
        file_name = path.basename(item)
        if ds_store in [file_name]:
            remove(item)
            dir_items.remove(item)
    dir_items.sort()


def readPDFOutline(pdf_fullpath: str) -> list:
    # MAKE NEW PDF NAME
    pdf_reader = PdfReader(pdf_fullpath, strict=False)

    pdf_outlines = pdf_reader.outline
    page_count = len(pdf_reader.pages)
    all_main_topics = []
    main_topic_name = None
    main_topic_page = None

    # MAIN-TOPIC
    for main_item in pdf_outlines:

        # SUB-TOPIC
        if isinstance(main_item, list):
            main_topic_object = MainTopic(name=main_topic_name, page=main_topic_page, endpage=page_count)
            for subitem in main_item:

                # MINI-TOPIC
                if isinstance(subitem, list):
                    first_item = True
                    for miniitem in subitem:
                        try:
                            _, miniitem_name = miniitem["/Title"].split(" - ")
                        except ValueError:
                            miniitem_name = miniitem["/Title"]
                        mini_topic_object = MiniTopic(name=miniitem_name, page=pdf_reader.get_destination_page_number(miniitem))
                        subtopic_object.addMiniTopic(mini_topic_object)
                        if first_item:
                            if mini_topic_object.page != subtopic_object.page:
                                subtopic_object.page = mini_topic_object.page
                            first_item = False

                else:
                    try:
                        _, subitem_name = subitem["/Title"].split(" - ")
                    except:
                        subitem_name = subitem["/Title"]
                    subtopic_object = SubTopic(name=subitem_name, page=pdf_reader.get_destination_page_number(subitem))

                main_topic_object.addSubtopic(subtopic_object)
            all_main_topics.append(main_topic_object)

        # MAIN TOPIC
        else:
            main_topic_name = main_item["/Title"]
            main_topic_page = pdf_reader.get_destination_page_number(main_item)

            # FIRST MAIN TOPIC
            if not len(all_main_topics) == 0:
                all_main_topics[-1].addEndpage(main_topic_page - 1)
    pdf_reader.close()

    return all_main_topics


def writePDFs(pdf_path: str, pdf_outline_list: list):

    pdf_directory_path = path.dirname(pdf_path)
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()

    all_pages = pdf_reader.pages

    for maintopic in pdf_outline_list:

        if maintopic.name == "Cardiology":

            maintopic_name = maintopic.name
            maintopic_page = maintopic.page
            maintopic_file_name = f"{maintopic_name}.pdf"
            maintopic_pdf_path = path.join(pdf_directory_path, maintopic_file_name)

            maintopic_page_object = pdf_writer.add_page(all_pages[maintopic_page])

            main_outline_item = pdf_writer.add_outline_item(title=maintopic_name, page_number=maintopic_page_object)

            print(maintopic_name)
            for subtopic in maintopic.subtopics:
                page_count = len(pdf_writer.pages) - 1
                print(f"PAGE COUNT = {page_count}")
                subtopic_object = maintopic.subtopics[subtopic]
                subtopic_name = subtopic_object.name
                subtopic_page = subtopic_object.page

                count = 1
                print(f"SUBTOPIC PAGE # = {subtopic_page}")
                while subtopic_page > page_count:
                    print("SUBTOPIC LARGER THAN PAGE COUNT")
                    page_count = len(pdf_writer.pages)-1
                    pdf_writer.add_page(all_pages[page_count + count])
                    count += 1
                subtopic_page_object = pdf_writer.add_page(all_pages[subtopic_page])
                subtopic_outline_item = pdf_writer.add_outline_item(title=subtopic_name, page_number=subtopic_page_object, parent=main_outline_item)

                print("\t", subtopic_name, subtopic_page)

                if len(subtopic_object.minitopics) != 0:
                    print("THIS SHOULD NOT PRINT")
                    for minitopic in subtopic_object.minitopics:
                        minitopic_object = subtopic_object.minitopics[minitopic]
                        minitopic_name = minitopic_object.name
                        minitopic_page = minitopic_object.page

                        count = 1
                        while minitopic_page > page_count:
                            page_count = len(pdf_writer.pages)-1
                            pdf_writer.add_page(all_pages[page_count + count])
                            count += 1

                        pdf_writer.add_page(all_pages[minitopic_page])
                        pdf_writer.add_outline_item(title=minitopic_name, page_number=minitopic_page, parent=subtopic_outline_item)
                        print("\t\t", minitopic_name, minitopic_page)
                    print()
            with open(maintopic_pdf_path, "wb") as output_file:
                pdf_writer.write(output_file)
            print()


def main() -> None:

    pdf_path = "/Users/diegoibarra/Media/Clinical/test/OnlineMedEd Notes.pdf"

    


if __name__ == "__main__":
    main()
