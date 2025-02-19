notes_path = "/Users/diegoibarra/Desktop/Medicine.md"
topics_path = "/Users/diegoibarra/Desktop/Medicine Topics.md"

with open(notes_path, "r") as open_file:
    raw_text = open_file.readlines()
    contents = [f"{line}\n" for line in raw_text if line.startswith("#")]

with open(topics_path, "w") as topics_file:
    topics_file.writelines(contents)
