file_name = input("Enter html file name: ")

f= open(file_name, "r")
text = f.read()
f.close()

def add_att(attr: str):
    target_list = []
    att.append('<' + attr + '>')


for att in target_list:
    text = text.replace(att, '')

