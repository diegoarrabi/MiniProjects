from os import path
from os import listdir
from os import remove


class SubTopic:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path
        self.lectures = []

    def addLectureList(self, lecture_list: list):
        self.lectures = lecture_list


class MainTopic:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path
        self.sub_topics = {}

    def addSubtopic(self, subtopic_object: SubTopic):
        self.sub_topics[subtopic_object.name] = subtopic_object


def removePrefixCount(item: str) -> str:
    while (item[0].isdigit()) or (item[0] == '.'):
        item = item[1:]
    return item


def sortTopics(dir_items: list[str], dir_path: str) -> list[str]:
    ds_store = ".DS_Store"
    pdf_item = ".pdf"
    dir_items.sort()
    if ds_store in dir_items:
        remove(path.join(dir_path, str(ds_store)))
        dir_items = dir_items.remove(ds_store)
    new_dir_items = [item for item in dir_items if not item.endswith(pdf_item)]
    return new_dir_items


def addLectures(topic_object: SubTopic, lectures_path: str) -> None:
    lectures_list = listdir(lectures_path)
    lectures_list.sort()
    lectures_list = [lecture.removesuffix(".mp4") for lecture in lectures_list]
    topic_object.addLectureList(lectures_list)


main_dir_path = "/Users/diegoibarra/Media/Clinical/BoardsBeyond"

general_topic_name = "1. General Topics"
main_topic_prefix = "#"
subtopic_prefix = "##"
lecture_prefix = "- [ ]"
indent_size = 1

main_topics_list = listdir(main_dir_path)
main_sorted_list = sortTopics(main_topics_list, main_dir_path)

# ITERATE THROUGH MAIN TOPICS
for main_topic_name in main_sorted_list:
    main_topic_path = path.join(main_dir_path, main_topic_name)
    main_topic = MainTopic(name=main_topic_name, path=main_topic_name)

    # MAKE SUBTOPIC LIST
    subtopics_list = listdir(main_topic_path)
    suptopic_sorted_list = sortTopics(subtopics_list, main_topic_path)

    # ITERATE THROUGH SUBTOPICS
    for subtopic_name in suptopic_sorted_list:
        general_topics = False
        subtopic_path = path.join(main_topic_path, subtopic_name)

        # SUBTOPIC CONTAINS LECTURES ONLY
        if (path.isfile(subtopic_path)) and (not general_topics):
            subtopic = SubTopic(general_topic_name, subtopic_path)
            addLectures(subtopic, main_topic_path)
            main_topic.addSubtopic(subtopic)
            break
        else:
            # SUBTOPIC CONTAINS MORE LECTURE TOPICS
            subtopic = SubTopic(subtopic_name, subtopic_path)
            subtopic_lectures_list = listdir(subtopic_path)
            sortTopics(subtopic_lectures_list, subtopic_path)
            addLectures(subtopic, subtopic_path)
            main_topic.addSubtopic(subtopic)

    print(f"# {removePrefixCount(main_topic.name)}")
    for count, subtopic in enumerate(main_topic.sub_topics):
        print(f"{subtopic_prefix}{removePrefixCount(subtopic)}")
        lectures_list = main_topic.sub_topics[subtopic].lectures
        for lecture_topic in lectures_list:
            item_prefix = f"{" "*indent_size}{lecture_prefix}"
            print(f"{item_prefix}{removePrefixCount(lecture_topic)}")
        print()
    print("")


