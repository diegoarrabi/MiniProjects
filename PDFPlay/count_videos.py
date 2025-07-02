

file = "/Users/diegoibarra/Media/Medical/BoardsBeyond/video.txt"

with open(file, "r") as openfile:
    lineslist = openfile.readlines()

# for i in lineslist:
#     print(i)

videos_list = [line for line in lineslist if line.rstrip().endswith(".mp4")]

# for i in videos_list:
#     print(i, end="")

print(len(videos_list))
