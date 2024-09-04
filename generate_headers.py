import csv
import os


def generate_book_table(title, author, year, country, genre, rating):
    table = f"""
| نام اثر | {title} |
| نویسنده | {author} |
| سال چاپ | {year} |
| کشور | {country} |
| ژانر | {genre} |
| امتیاز | {rating} |
"""
    return table


folder_path = "_posts"
with open('table_of_posts.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)
    for row in spamreader:
        file_path = os.path.join(folder_path, row[5] + '-' + row[6])
        print(file_path)
        file_contents = ''
        changed = False
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            if 'نام اثر' not in file_contents:
                rating = '⭐'*int(row[7]) + '☆'*(10-int(row[7])) + ' ' + row[7] + '/10'

                header_for_book = generate_book_table(row[0],row[1],row[2],row[3],row[8],rating)
                #print(header_for_book)
                text = """toc: true\n---"""
                text2 = """]
tags: ["""
                
                file_contents = file_contents.replace(text, text+'\n\n' + header_for_book)
                if rating not in file_contents:
                    file_contents = file_contents.replace(text2, ','+rating+text2)

                file_contents = file_contents + """

### شخصیت ها
- شخصیت اول: پدر خانواده
- شخصیت دوم: مادر خانواده

### قسمت کوتاهی از شروع رمان
در این رمان، نویسنده از زبان پدر خانواده روایت می کند.

### موضوع فصل‌ها
- فصل اول: تیتر اول
  - زیر فصل اول
    - زیر فصل زیر فصل اول

### وقایع‌نگاری
- وقایع‌نگاری فصل اول

### نظر شخصی



"""
                
                changed = True
            
        if changed:
           print(file_contents)
           with open(file_path, 'w', encoding='utf-8') as file:
               pass
               file.write(file_contents)
        #break
        
        



# for filename in os.listdir(folder_path):
#     if filename.endswith(".md"):
#         file_path = os.path.join(folder_path, filename)
#         print(file_path)
#         # Read the file contents
#         with open(file_path, 'r', encoding='utf-8') as file:
#             file_contents = file.read()
#             if 'نام اثر' not in file_contents:
#                 pass#print(file_path)