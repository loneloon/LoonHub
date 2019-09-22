import urllib.request

def html_killer(page: str):
    fp = urllib.request.urlopen(page)
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

    add_att(['tr', 'head', 'body', 'html', 'head', 'h1', 'table', 'title', 'span', 'td', 'th', 'td align="right"', 'a', 'td valign="top"', 'th colspan="5"', 'hr'])

    for att in target_list:
        text = text.replace(att, '')


    return text