first = "buhuhuhu, c, d, a, b, dhhuhuhuhu, chuhuh, ahuhuh"
second = "huhuhuuhhu, c, a, uhhuhuhuhu"
fir_seq = []
sec_seq = []
fir_seq = first.split(", ")
sec_seq = second.split(", ")
fir_seq = sorted(fir_seq)
sec_seq = sorted(sec_seq)

result = []
for i in fir_seq:
    if i in sec_seq:
        result.append(i)
    else:
        pass
result = ','.join(result)
print(result)