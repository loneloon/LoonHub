elements = [2, 2,]

# This code checks if all elements in the given list are equal and returns a bool (True/False)

result = True

if len(elements) <= 1:
    print('1 or less elements')
else:
    first_l = elements[0]
    for x in elements:
        if x == first_l:
            continue
        else:
            result = False
            break
    print(result)