

def gcd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


m = int(input("M = "))
n = int(input("N = "))
k = int(input("K = "))

print(m+n+k-(gcd(m, n) + gcd(m, k) + gcd(n, k)) + gcd(m, gcd(n, k)) - 1)
