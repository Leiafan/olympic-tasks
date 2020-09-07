from math import *

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
d = a3
result = []
divs = [1]

for i in range(2, int(sqrt(abs(d)))+1):
    if d % i == 0:
        divs.extend([i, d/i])
divs.extend([d])

for i in divs:
    if((i + a1)*i+a2)*i+a3 == 0:
        result.append(i)
    if ((-i + a1)*-i+a2)*-i+a3 == 0:
        result.append(-i)

print("result: ", result)
