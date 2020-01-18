text = "7654[b]You may input any text you want and it will come out clean[/b]98679123hhjnkjvjhg"

print(text)

begin = '[b]'
end = '[/b]'

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
    print("")
else:
    print(target)

# It works pretty well btw!
