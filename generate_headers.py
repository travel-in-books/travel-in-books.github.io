def generate_book_table(title, author, year, country, genre, rating):
    table = f"""
| نام اثر        | {title}       |
| نویسنده        | {author}      |
| سال چاپ        | {year}        |
| کشور           | {country}     |
| ژانر           | {genre}       |
| امتیاز         | {rating}      |
"""
    return table