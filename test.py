import os
path = "sections"
sections_path = "sections"

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for i in files:
    if i.endswith(".pdf"):
        print(i)