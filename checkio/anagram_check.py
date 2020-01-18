

def verify_anagrams(first_word, second_word):
    import string
    alphabet = string.ascii_letters[:28]
    fwd = {}
    fwdd ={}
    swd = {}
    swdd = {}
    for i in first_word.lower():
        if i != ' ':
            fwd[i] = first_word.lower().count(i)
        else:
            pass
    for i in second_word.lower():
        if i != ' ':
            swd[i] = second_word.lower().count(i)
        else:
            pass
    result = True
    fwds = sorted(fwd.keys(), key=alphabet.index, reverse=True)
    for i in fwds:
        fwdd[i] = fwd.get(i)
    swds = sorted(swd.keys(), key=alphabet.index, reverse=True)
    for i in swds:
        swdd[i] = swd.get(i)
    print(fwdd)
    print(swdd)
    if fwdd == swdd:
        pass
    else:
        result = False
    return result
print(verify_anagrams("Programming", "Gram Ring Mop"))
