data = 'jhkajhds678768'

upper = False
lower = False
digit = False
length = False

if len(data) >= 10:
    length = True
else:
    pass

data_list = []
for char in data:
    data_list.append(char)

for char in data_list:
    if char.isdigit():
        digit = True
    else:
        pass

for char in data_list:
    if char.islower():
        lower = True
    else:
        pass

for char in data_list:
    if char.isupper():
        upper = True
    else:
        pass

if upper == True and lower == True and digit == True and length == True:
    print(True)
else:
    print(False)

# IT WORKS!
