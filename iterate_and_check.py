import os

directory = './_posts/'

data = []
selected_file_names = []
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            if 'تیتر انگلیسی<sup id="a1">[1](#f1)</sup>' not in content:
                if '[1](#f1)</sup>' not in content:
                    selected_file_names.append(filename)
