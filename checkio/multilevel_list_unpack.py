array = [-1,[1,[-2,[3],[[5],[10,-11],[1,100,[-1000,[5000]]],[20,-10,[[[]]]]]]]]

print(len(array))

if len(array) == 0:
    print([])
else:
    a1 = str(array).replace("]", "")
    a2 = a1.replace("[", "")
    a3 = a2.split(", ")
    a4 = []
    for i in a3:
        if bool(i) == True:
            a4.append(int(i))
        else:
            pass
    print(a4)
