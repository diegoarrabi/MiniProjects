
import os
import subprocess
import time


class Video:
    def __init__(self, filepath: str, mainpath: str):
        self.main_path = mainpath
        self.path = filepath
        self.name: str
        self.topic_name: str
        self.duration_sec: float
        self.__getName()
        self.__getSeconds()

    def __getSeconds(self):
        cmd = subprocess.run([
            "ffprobe",
            "-v",
            "error",
            "-of",
            "csv=p=0",
            "-show_entries",
            "format=duration",
            self.path
        ],
            capture_output=True,
            text=True
        )
        if cmd.returncode == 1:
            exit(print(cmd.stderr))
        try:
            self.duration_sec = round(float(cmd.stdout))
        except ValueError:
            exit(print(f"{cmd.stdout} NOT A FLOAT"))

    def __getName(self):
        self.name, _ = os.path.splitext(os.path.basename(self.path))
        topic_split = (self.path.replace(self.main_path, "").removeprefix("/")).split("/")
        topic_split = topic_split[:-1]
        self.topic_name = topic_split[0]


def timeString(total_seconds: float):
    # if total_seconds >= 3600:
    hours = int(total_seconds // 3600)
    minutes = int(total_seconds % 3600) // 60
    # seconds = int(total_seconds % 60)
    time = f"{hours:02d}:{minutes:02d}"
    return time


PARENT_DIRECTORY = os.path.join(os.path.expanduser("~"), "Media", "Medical", "BoardsBeyond")
# PARENT_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources", "videos")

# cmd = subprocess.run(["ls", "-R", PARENT_DIRECTORY], capture_output=True, text=True)
# output = cmd.stdout
# error = cmd.stderr

# current_directory = ""
# skip = True

# all_videos: list[Video] = []
# videos_dict: dict[str, int] = {}

# for line in output.splitlines():
#     line = line.replace(":", "")

#     if os.path.isdir(line):
#         skip = False
#         current_directory = line
#     else:
#         if skip:
#             continue
#         if line.endswith(".mp4"):
#             line = os.path.join(current_directory, line)
#             all_videos.append(Video(line, PARENT_DIRECTORY))


# for video in all_videos:
#     if not videos_dict.get(video.topic_name):
#         videos_dict[video.topic_name] = video.duration_sec
#     else:
#         videos_dict[video.topic_name] += video.duration_sec

# videos: list[tuple[int, str]] = []

# for topic in videos_dict:
#     topic_name = f"{topic[4:]} "
#     topic_seconds = videos_dict[topic]
#     videos.append((topic_seconds, topic_name))

# videos.sort(reverse=True)

# with open("TopicTime.txt", "w",) as writeFile:
#     for sorted in videos:
#         # writeFile.write(f"{sorted[1]:-<35} {timeString(sorted[0])}\n")
#         writeFile.write(f"{sorted[1]}\n")
#         # writeFile.write(f"{sorted[1]}-{(sorted[0])}\n")
#         # writeFile.write(f"[{timeString(sorted[0])}]\n")

topics_list = [os.path.join(PARENT_DIRECTORY, path)
               for path in os.listdir(PARENT_DIRECTORY)
               if not path.startswith(".")
               and os.path.isdir(os.path.join(PARENT_DIRECTORY, path))
               ]

# for topic in topics_list:
#     topic_filename = f"{os.path.basename(topic)[4:]}.md"
#     topic_fullpath = os.path.join(topic, topic_filename)
#     if not os.path.exists(topic_fullpath):
#         # subprocess.run(["touch", topic_fullpath])
#         # time.sleep(0.2)
#     # subprocess.run(["open", topic_fullpath])
#     print(topic_fullpath)

# exit()


with open("TopicTime.txt", "r",) as writeFile:
    videos = writeFile.readlines()

for index, item in enumerate(videos):
    item = item.strip().rstrip()
    item_name, item_time = item.split("-")
    videos[index] = item_name, int(item_time)


max_string = max(list(map(lambda topic: len(topic[0]), videos)))

last_index = len(videos)-1
for count in range(round(len(videos)/2)):
    video_1 = videos[last_index-count]
    video_2 = videos[count]
    total_time = timeString(video_1[1] + video_2[1])
    print(f"{video_1[0]:-<{max_string}} {video_2[0]:-<{max_string}} {total_time}")
