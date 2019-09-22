class Trans:
    syllables = {'iia': 'ия', 'aia': 'ая', 'aya': 'ая', 'shch': 'щ', 'sch': 'щ', 'ii': 'ьи', 'ia': 'ия', 'iy': 'ий', 'yi': 'ьи', 'kh': 'х', 'ch': 'ч',
                 'sh': 'ш', 'ya': 'ья', 'ay':'ай', 'tz': 'ц', 'ts': 'ц', 'th': 'т'}
    letters = {'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'х', 'j': 'ж',
                'q': 'к', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т',
              'u': 'у', 'v': 'в', 'w': 'в', 'x': 'кс', 'y': 'ы', 'i': 'и', 'z': 'з'}

# YOU NEED TO SORT SYLLABLES INTO SEVERAL CATEGORIES BASED ON THEIR INITIAL PLACEMENT!!!

def tl(text: str):
    for eng, rus in Trans.syllables.items():
        if eng.replace(eng, eng.upper()) in text:
            text = text.replace(eng.replace(eng, eng.upper()), rus.replace(rus, rus.upper()))
        else:
            pass
        if eng.replace(eng[0], eng[0].upper()) in text:
            text = text.replace(eng.replace(eng[0], eng[0].upper()), rus.replace(rus[0], rus[0].upper()))
        else:
            pass
        if eng in text:
            text = text.replace(eng, rus)
        else:
            pass
    for eng, rus in Trans.letters.items():
        if eng.upper() in text:
            text = text.replace(eng.upper(), rus.upper())
        else:
            pass
        if eng in text:
            text = text.replace(eng, rus)
        else:
            pass
    return text

print(tl("Roman Tarnavskii"))





