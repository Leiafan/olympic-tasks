from math import *


def gfs(x):
    g = x
    while x % (g**2) != 0:
        g -= 1
    return g


def gcd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < 0:
    a = -a
    b = -b
    c = -c
D = b**2 - 4*a*c

if D < 0:
    print("Equation has no roots")
    exit(0)

A = 2*a
B = -b
if D == 0:
    x = B/A
    print("x = ", x)
    exit(0)
d = gfs(D)
E = D//d**2
f = gcd(abs(d), abs(a))

if sqrt(D) != int(sqrt(D)):
    if A == 1:
        if b <= 0:
            print("x = ", -b, "+- sqrt(", D, ")")
        else:
            print("x = -", b, "+- sqrt(", D, ")")
    else:
        if b <= 0:
            print("x = (", -b, "+- sqrt(", D, "))/", A)
        else:
            print("x = (-", b, "+- sqrt(", D, "))/", A)
else:
    if b <= 0:
        if int(b / A) == b / A and int(sqrt(D) / A) == sqrt(D) / A:
            print("x = ", -b / A, "+- ", sqrt(D) / A)
        else:
            print("x = ", -b, "/", A, "+- ", sqrt(D), "/",A)
    else:
        if int(b / A) == b / A and int(sqrt(D) / A) == sqrt(D) / A:
            print("x = -", b / A, "+- ", sqrt(D) / A)
        else:
            print("x = -", b / A, "+- ", sqrt(D) / A)
