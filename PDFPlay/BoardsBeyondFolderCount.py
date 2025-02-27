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


def sortTopics(dir_items: list[str], dir_path: str) -> None:
    ds_store = ".DS_Store"
    dir_items.sort()
    if ds_store in dir_items:
        remove(path.join(dir_path, str(ds_store)))
        dir_items = dir_items.remove(ds_store)


def addLectures(topic_object: SubTopic, lectures_path: str) -> None:
    lectures_list = listdir(lectures_path)
    lectures_list.sort()
    lectures_list = [lecture.removesuffix(".mp4") for lecture in lectures_list]
    topic_object.addLectureList(lectures_list)


main_dir_path = "/Users/diegoibarra/Media/Medicine Videos/Clinical/BoardsBeyond"

general_topic_name = "1. General Topics"
main_topic_prefix = "#"
subtopic_prefix = "##"
lecture_prefix = "- [ ]"
indent_size = 1

main_topics_list = listdir(main_dir_path)
sortTopics(main_topics_list, main_dir_path)

# ITERATE THROUGH MAIN TOPICS
for main_topic_name in main_topics_list:
    main_topic_path = path.join(main_dir_path, main_topic_name)
    main_topic = MainTopic(name=main_topic_name, path=main_topic_name)

    # MAKE SUBTOPIC LIST
    subtopics_list = listdir(main_topic_path)
    sortTopics(subtopics_list, main_topic_path)

    # ITERATE THROUGH SUBTOPICS
    for subtopic_name in subtopics_list:
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


# all_topics = os.listdir(main_dir)
# all_topics.sort()

# topic_breakdown = {"Topic_Name": "", "Sub_Topic_Name": {}}


# for topic in all_topics:
#     topic_video_count = 0
#     topic_path = os.path.join(main_dir, topic)
#     if os.path.basename(topic_path).startswith("."):
#         continue
#     topic_breakdown["Topic_Name"] = topic

#     all_subtopics = os.listdir(topic_path)
#     all_subtopics.sort()

#     for sub_topic in all_subtopics:
#         topic_items = []
#         sub_topic_video_count = 0
#         sub_topic_path = os.path.join(topic_path, sub_topic)
#         if os.path.basename(sub_topic_path).startswith("."):
#             continue

#         if os.path.isdir(sub_topic_path):
#             sub_topic_items = []
#             topic_breakdown["Sub_Topic_Name"] = {sub_topic: sub_topic_items}

#             all_sub_topic_items = os.listdir(sub_topic_path)
#             all_sub_topic_items.sort()

#             for sub_topic_item in all_sub_topic_items:
#                 sub_topic_item_path = os.path.join(sub_topic_path, sub_topic_item)
#                 if os.path.basename(sub_topic_path).startswith("."):
#                     continue
#                 sub_topic_items.append(sub_topic_item)
#                 topic_video_count += 1
#                 sub_topic_video_count += 1

#         elif os.path.isfile(sub_topic_path):
#             topic_items.append(sub_topic)
#             topic_breakdown["Sub_Topic_Name"] = {"General Topics": topic_items}
#             topic_video_count += 1
#             sub_topic_video_count += 1

#     print(topic_breakdown["Topic_Name"])
#     print(topic_breakdown["Sub_Topic_Name"])
#     # print(f"{topic}: {topic_video_count} Videos", end="\n\n")
