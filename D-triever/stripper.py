def cut(text: str, begin: str, end: str):
    if begin in text and end in text:
        first_symb_pos = text.find(begin) + len(begin)
        last_symb_pos = text.find(end)
    elif begin in text:
        first_symb_pos = text.find(begin) + len(begin)
        last_symb_pos = None
    elif end in text:
        first_symb_pos = 0
        last_symb_pos = text.find(end)
    else:
        first_symb_pos = 0
        last_symb_pos = None

    target = text[first_symb_pos:last_symb_pos]

    if first_symb_pos == last_symb_pos:
        return ""
    else:
        return target
