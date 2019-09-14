import urllib.request

fp = urllib.request.urlopen("http://loneloon.net/")
mybytes = fp.read()

text = mybytes.decode("utf8")
fp.close()


target_list = []

def add_att(attr: list):
    for each in attr:
        each1 = '<' + each + '>'
        target_list.append(each1)
        each2 = '</' + each + '>'
        target_list.append(each2)

add_att(['tr', 'head', 'body', 'html', 'head', 'h1', 'table', 'title'])

for att in target_list:
    text = text.replace(att, '')


print(target_list)
