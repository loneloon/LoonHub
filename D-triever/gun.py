import stripper
import data_cues

f= open("TestRawHTML.html", "r")
text = f.read()
f.close()

strip_atts = ['</td></tr><tr><td class="line-number" value=', '<span class="html-tag">', '<span class="html-attribute-name">',
              '></td><td class="line-content">', '<span class="html-attribute-value">', '<div>', '</div>', '<div', '</div']

text = text.replace('&lt;', '<')
text = text.replace('&gt;', '>')

for att in strip_atts:
    text = text.replace(att, '')

print(stripper.cut(text, data_cues.FullName.start, data_cues.FullName.end))
#print(stripper.cut(text, data_cues.Email.start, data_cues.Email.end))
#print(stripper.cut(text, data_cues.DoB.start, data_cues.DoB.end))
#print(stripper.cut(text, data_cues.Phone.start, data_cues.Phone.end))

#print(text)
