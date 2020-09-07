from math import *


def min9():
    #m = 3.321
    #k = 3.321

    N1 = 1
    while log10(9.99) > log10(N1) % 1:
        N1 *= 2

    N2 = 1
    while log10(9.99) > log10(N2) % 1:
        N2 *= 5
    return N2


print("N = " + str(min9()))
