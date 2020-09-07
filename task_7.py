

def decToTriple(N, check):
    while N != int(N):
        N *= 10
    base = 3
    y = []
    while N > 0:
        y.append(N % base)
        N //= base
    y.reverse()
    while check != 0:
        if y[int(N)] == 1:
            return "No"
        check -= 1
        N += 1
    return "Yes"


a = int(input("a = "))
b = int(input("b = "))
n = int(input("n = "))

c = a // b
d = (a - c*b)/b

print(str(decToTriple(d, n)))
