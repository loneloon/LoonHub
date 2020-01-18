import math

data = sorted([4,4,4])
a = data[0]
b = data[1]
c = data[2]

cosA = (b**2 + c**2 - a**2)/(2*b*c)
cosB = (c**2 + a**2 - b**2)/(2*c*a) # cosB... YEEEEEET!
cosC = (a**2 + b**2 - c**2)/(2*c*a)

print(cosA,cosB,cosC)

result = []
if cosA >= 1 or cosB >= 1 or cosC >= 1:
    result = [0, 0, 0]
elif cosA <= -1 or cosB <= -1 or cosC <= -1:
    result = [0, 0, 0]
else:
    A = round(math.degrees(math.acos(cosA)))
    result.append(A)
    B = round(math.degrees(math.acos(cosB)))
    result.append(B)
    result.append(180 - A - B)
print(result)