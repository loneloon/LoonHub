list_input = [1,2,3,1,2]

control_l = []

for el in list_input:
    if list_input.count(el) > 1:
        control_l.append(el)
    else:
        pass

print(control_l)


