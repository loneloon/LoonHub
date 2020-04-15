with open("history", "r") as h:
    tot = len(h.readlines())
with open("history", "r") as h:
    for idx, i in enumerate(h.readlines()):
        if tot > 5:
            if idx > tot - 6:
                print(i[:-1])
        else:
            print(i[:-1])