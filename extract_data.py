import os
import yaml
import pandas as pd

# Directory where your files are stored (change this to your directory)
directory = './_posts/'

# Initialize a list to store the data for each file
data = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        # Read the file content
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

            # Extract the YAML front matter (the part between ---)
            if content.startswith("---"):
                # Find the end of the YAML block
                end_index = content.find("---", 3)
                if end_index != -1:
                    yaml_content = content[3:end_index].strip()
                    yaml_data = yaml.safe_load(yaml_content)

                    # Extract the table content after the YAML (lines starting with | )
                    table_data = {}
                    table_start = content.find('|', end_index)
                    if table_start != -1:
                        table_lines = content[table_start:].splitlines()
                        for line in table_lines:
                            if line.startswith('|'):
                                # Split the table line into key-value pairs
                                columns = line.split('|')
                                if len(columns) > 2:
                                    key = columns[1].strip()
                                    value = columns[2].strip()
                                    table_data[key] = value

                    # Append the data to the list (combining YAML and table data)
                    data.append({
                        'file_name': filename,
                        'title': yaml_data.get('title', ''),
                        'categories': ', '.join(yaml_data.get('categories', [])),
                        'tags': ', '.join(yaml_data.get('tags', [])),
                        'toc': yaml_data.get('toc', False),
                        'work_name': table_data.get('نام اثر', ''),
                        'author': table_data.get('نویسنده', ''),
                        'year': table_data.get('سال چاپ', ''),
                        'country': table_data.get('کشور', ''),
                        'genre': table_data.get('ژانر', ''),
                        'literary_school': table_data.get('مکتب ادبی', ''),
                        'rating': table_data.get('امتیاز', '')
                    })

# Convert the data into a DataFrame
df = pd.DataFrame(data)
df.to_csv('data.csv')
print(df['country','title'].head())

# Display the table to the user
#import ace_tools as tools; tools.display_dataframe_to_user(name="Books Table", dataframe=df)
