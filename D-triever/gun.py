import stripper
import data_cues

f= open("TestRawHTML2.html", "r")
text = f.read()
f.close()

strip_atts = ['</td></tr><tr><td class="line-number" value=', '<span class="html-tag">', '<span class="html-attribute-name">',
              '></td><td class="line-content">', '<span class="html-attribute-value">', '<div>', '</th>', '</div>', '<div', '</div', '</tbody>', '</span>', '</tr>', '<th>', '<tbody>', '<td>', '</td>']
text = text.replace('&lt;', '<')
text = text.replace('&gt;', '>')

for att in strip_atts:
    text = text.replace(att, '')

candidate_name = stripper.cut(text, data_cues.FullName.start, data_cues.FullName.end)
candidate_email = stripper.cut(text, data_cues.Email.start, data_cues.Email.end)
candidate_dob = stripper.cut(text, data_cues.DoB.start, data_cues.DoB.end)
candidate_mob = stripper.cut(text, data_cues.Phone.start, data_cues.Phone.end)

#print(candidate_name)
#print(candidate_email)
#print(candidate_dob)
#print(candidate_mob)


print(text)
