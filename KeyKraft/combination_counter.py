def comb_count(data: list):
    counter = 0

    for i in range(len(data)+1):
        counter += i**len(data)

    return counter
