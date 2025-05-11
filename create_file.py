import datetime
import re

def format_filename(title, author):
    # Replace spaces with hyphens and remove non-alphanumeric characters
    title_part = re.sub(r'\W+', '-', title).strip('-')
    author_part = re.sub(r'\W+', '-', author).strip('-')
    date_part = datetime.date.today().isoformat()
    filename = f"{date_part}-{title_part}-by-{author_part}.md"
    return filename

def create_book_file(title, author, country, genre, pub_date):
    filename = format_filename(title, author)
    
    frontmatter = f"""---
title: {title} by {author}
categories: [{genre},Fiction Literature]
tags: [{country},Story]
---     
| Title | {title}  |
| Author |  {author}  |
| Publication Date | {pub_date}   |
| Country | {country} |
| Genre | {genre}  |
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(frontmatter)
    
    print(f"File '{filename}' created successfully.")

# Example usage:
if __name__ == "__main__":
    title = input("Enter the book title: ").strip()
    author = input("Enter the author name: ").strip()
    country = input("Enter the country: ").strip()
    genre = input("Enter the genre: ").strip()
    pub_date = input("Enter the publication year: ").strip()

    create_book_file(title, author, country, genre, pub_date)
