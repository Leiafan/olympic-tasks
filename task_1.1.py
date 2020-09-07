# By natural numbers a, n find number М, which equals
# two lower digits of power N = a^n. 

a = int(input("a = "))
n = int(input("n = "))


def exp(x, k):
    if k == 0:
        return 1
    if k % 2 == 0:
        return exp(x, k/2)**2
    return x*exp(x, k-1)


N = exp(a, n) % 100

print("N = " + str(N))
