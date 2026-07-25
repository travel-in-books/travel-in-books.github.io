import os
import re
import sys

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


# --- rating consistency check -------------------------------------------------
# Every post carries its rating twice: once as a hardcoded star string in the
# frontmatter `tags:` line, and once as `{% include rating.html score=N %}` in
# the metadata table. Nothing keeps the two in sync, so check them here.

STARS = re.compile(r'([⭐☆]+)\s*(\d+)/10')
TAGS_LINE = re.compile(r'^tags:.*$', re.MULTILINE)
SCORE_ROW = re.compile(r'^\|\s*امتیاز\s*\|.*?score=(\d+)', re.MULTILINE)
ANY_SCORE = re.compile(r'include\s+rating\.html\s+score=(\d+)')


def check_stars(star_string, score):
    """A star string must be 10 glyphs: `score` filled followed by the rest empty."""
    expected = '⭐' * score + '☆' * (10 - score)
    return star_string == expected, expected


def check_post(path):
    """Return a list of human-readable problems found in one post."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    problems = []

    tags_match = TAGS_LINE.search(content)
    tag_score = None
    if not tags_match:
        problems.append('no `tags:` line in frontmatter')
    else:
        tag_stars = STARS.search(tags_match.group(0))
        if not tag_stars:
            problems.append('no rating tag (e.g. `⭐⭐⭐⭐⭐⭐⭐☆☆☆ 7/10`) in `tags:`')
        else:
            stars, tag_score = tag_stars.group(1), int(tag_stars.group(2))
            if tag_score > 10:
                problems.append(f'rating tag score {tag_score} is above 10')
            else:
                ok, expected = check_stars(stars, tag_score)
                if not ok:
                    problems.append(
                        f'rating tag stars do not match its own score: '
                        f'`{stars} {tag_score}/10` should be `{expected} {tag_score}/10`'
                    )

    # The metadata table's امتیاز row is the book-level score. Collections such
    # as the Murakami post repeat the table per story; the frontmatter tag
    # tracks the first one.
    row_match = SCORE_ROW.search(content)
    if not row_match:
        problems.append('no `| امتیاز |` row with `{% include rating.html score=N %}`')
    else:
        row_score = int(row_match.group(1))
        if tag_score is not None and row_score != tag_score:
            problems.append(
                f'rating tag says {tag_score}/10 but the امتیاز row says score={row_score}'
            )

    for score in (int(s) for s in ANY_SCORE.findall(content)):
        if score > 10:
            problems.append(f'`score={score}` is above 10')

    # Raw star strings in the body (per-story ratings written by hand). Scan the
    # body only, so the frontmatter tag is not reported twice.
    parts = content.split('---\n', 2)
    body = parts[2] if len(parts) == 3 else content
    for stars, score in STARS.findall(body):
        score = int(score)
        if score > 10:
            continue  # already reported above
        ok, expected = check_stars(stars, score)
        if not ok:
            problems.append(
                f'body stars do not match their score: '
                f'`{stars} {score}/10` should be `{expected} {score}/10`'
            )

    return problems


def check_ratings():
    failures = 0
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith('.md'):
            continue
        problems = check_post(os.path.join(directory, filename))
        if problems:
            failures += 1
            print(filename)
            for problem in problems:
                print(f'  - {problem}')
    return failures


if __name__ == '__main__':
    failures = check_ratings()
    total = len([f for f in os.listdir(directory) if f.endswith('.md')])
    if failures:
        print(f'\n{failures} of {total} posts have rating problems.')
        sys.exit(1)
    print(f'All {total} posts have consistent ratings.')
