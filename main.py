from typing import List

def paginate(string: str, amount_of_chars: int) -> List[str]:
    pages = []
    mi = 0
    for i in range(0, len(string) + 5):
        if i % amount_of_chars == 0 and i != 0:
            mi = i
            pages.append(string[mi:i])
    if mi < len(string):
        pages.append(string[mi:])
    return pages
