import os
path = "sections"
sections_path = "sections"

path_file = str(sections_path +"\\")
files = os.listdir(sections_path)
for i in files:
    if i.endswith(".pdf"):
        print(i)