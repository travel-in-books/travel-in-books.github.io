import csv
import os

def replace_string_in_files(directory, target_string, replacement_string):
    """
    Replaces all occurrences of target_string with replacement_string in all .md files within the specified directory.

    :param directory: Path to the directory containing .md files
    :param target_string: The string to be replaced
    :param replacement_string: The string to replace with
    """
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    new_content = content.replace(target_string, replacement_string)
                    
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    
                    print(f"Replaced text in: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

def print_files_without_string(folder_path, search_string):
    # Iterate over all the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            
            # Read the file contents
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()
            
            # Check if the file does not contain the search string
            if search_string not in file_contents:
                print(f"File does not contain the string: {filename}")

def print_all_posts(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            print(filename)


def extract_infos(input_string,writer):
    import re

    # Regular expressions to capture title, categories, and tags
    title_pattern = r'title:\s*(.*)'
    categories_pattern = r'categories:\s*\[(.*?)\]'
    tags_pattern = r'tags:\s*\[(.*?)\]'

    # Extracting the title
    title_match = re.search(title_pattern, input_string)
    title = title_match.group(1).strip() if title_match else None

    # Extracting the categories
    categories_match = re.search(categories_pattern, input_string)
    categories = categories_match.group(1).split(',') if categories_match else []

    # Extracting the tags
    tags_match = re.search(tags_pattern, input_string)
    tags = tags_match.group(1).split(',') if tags_match else []

    # Output
    az = ' از '
    print(title)
    if az in title:
        title_author=title.rsplit(az,maxsplit=1)
        writer.writerow([title_author[1].strip(),title_author[0].strip()])
            
    
    #print("Title:", title_author)
    #print("Categories:", [category.strip() for category in categories])
    #print("Tags:", [tag.strip() for tag in tags])

    #return title, 

def get_files_for_extract_info(folder_path):
    with open('table_of_posts.csv', 'w') as csvfile:
        fieldnames = ['title', 'author', 'year']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for filename in os.listdir(folder_path):
            if filename.endswith(".md"):
                file_path = os.path.join(folder_path, filename)
                print(file_path)
                # Read the file contents
                with open(file_path) as input_file:
                    file_contents = input_file.read()
                    extract_infos(file_contents,writer)


if __name__ == "__main__":
    directory_path = "_posts"  # Specify your directory path here
    search_text = "پینهاد سروش روحبخش"  # Specify the text you want to replace
    replace_text = "پیشنهاد سروش روحبخش"  # Specify the replacement text

    #replace_string_in_files(directory_path, search_text, replace_text)

    # Example usage
    folder_path = "_posts"
    search_string = "### نظر شخصی"

    #print_files_without_string(folder_path, search_string)

    #print_all_posts(folder_path)

    get_files_for_extract_info(folder_path)
