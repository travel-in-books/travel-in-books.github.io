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

if __name__ == "__main__":
    directory_path = "_posts"  # Specify your directory path here
    search_text = "پینهاد سروش روحبخش"  # Specify the text you want to replace
    replace_text = "پیشنهاد سروش روحبخش"  # Specify the replacement text

    #replace_string_in_files(directory_path, search_text, replace_text)

    # Example usage
    folder_path = "_posts"
    search_string = "### نظر شخصی"

    print_files_without_string(folder_path, search_string)
