import os

def get_files_by_type(type: str):
    for root, __, files in os.walk("c:/"):
        for file in files:
            if file.endswith(f".{type}"):
                yield os.path.join(root, file)

for i in get_files_by_type(".old"):
    print(i)