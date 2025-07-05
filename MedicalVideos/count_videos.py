import os
import subprocess


class Item:
    def __init__(self, path: str):
        self.isdir: bool = os.path.isdir(path)
        self.isfile: bool
        self.path = path
        self.item_name: str = os.path.basename(path).upper()
        self.contents: list

    def dirContents(self):
        self.isfile = not self.isdir
        if self.isdir:
            self.contents = [os.path.join(self.path, name) for name in os.listdir(self.path)
                             if not name.startswith(".") and not name.lower().endswith(".pdf")]
    
    
    


class VideoTopic:
    def __init__(self, directory: str):
        self.path = directory
        self.topic_name: str = os.path.basename(directory).upper()
        self.contents: list[Item] = []
        self.dirContents()

    def dirContents(self):
        content_paths = [os.path.join(self.path, name) for name in os.listdir(self.path)
                         if not name.startswith(".") and not name.lower().endswith(".pdf")]
        for item in content_paths:
            self.contents.append(Item(item))
        

    def iterDir(self, path: Item):
        if path.isfile: 
            print("IS FILE")
        

    def printContents(self):
        print(self.topic_name)




PARENT_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources", "videos")
topics_list = [os.path.join(PARENT_DIRECTORY, path) for path in os.listdir(PARENT_DIRECTORY) if not path.startswith(".")]

all_topics_list: list[VideoTopic] = []

for topic_path in topics_list:
    all_topics_list.append(VideoTopic(topic_path))

for item in all_topics_list:
    print(item.topic_name)
    item.printContents()
