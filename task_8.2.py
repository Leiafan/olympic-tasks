

a = int(input("a = "))


def sq_equation(x):
    if x == 0:
        return 0
    if x == 1:
        return -1, 1
    if x < 0:
        return


def gfs(x):
#    g = x/2
    g = x
    while x % (g**2) != 0:
        g -= 1
    return g


d = gfs(a)
if d == 1:
    print("x = +-", d, "* sqrt(", a**2, ")")
else:
    print("x = +-", d, "* sqrt(", a, ")")
