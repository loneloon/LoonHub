file_name = input("Enter html file name: ")

f= open(file_name, "r")
text = f.read()
f.close()

target_atts = ['</td></tr><tr><td class="line-number" value=', '<span class="html-tag">', '<span class="html-attribute-name">',
              '></td><td class="line-content">', '<span class="html-attribute-value">', '<div>', '</div>', '<div', '</div']

for att in strip_atts:
    text = text.replace(att, '')

