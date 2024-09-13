import os
import re

def contains_number_dot(text):
    # Regular expression to match a number followed by a dot
    pattern = r'\d+\.'  
    # Search for the pattern in the text
    match = re.search(pattern, text)
    # Return True if match is found, else False
    return bool(match)

output = ''
content = ''
title = ''
with open('faslha','r') as file:
    for line in file:      
        if contains_number_dot(line):
            if title != '':
                output = output + f'''
<details>
<summary>{title}</summary>
{content}
</details>'''
            title = line.rstrip()
            content = ''
        else:
            content = content + line
    
    with open('converted_faslha', 'w') as fw:
        fw.write(output) 
        