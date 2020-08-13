from typing import List

def paginate(string: str, amount_of_chars: int) -> List[str]:
    pages = []
    mi = 0
    for i in range(0, len(string)):
        elem = ""
        if i % amount_of_chars == 0 and i != 0:
            elem = string[mi:i]
            mi = i
            pages.append(elem)
    if mi < len(string):
        elem = string[mi:]
        pages.append(elem)
    return pages
