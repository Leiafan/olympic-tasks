#

a = int(input("a = "))
b = int(input("b = "))


def gcd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def linear_solve(x, y, g):
    if y == 0:
        return 0
    if x < 0 or y < 0:
        print(str((y/g)/(x/g)))
        return -(y/g)/(x/g)
    else:
        print(str((y/g)/(x/g)))
        return (y/g)/(x/g)


d = gcd(abs(a), abs(b))

linear_solve(a, b, d)
