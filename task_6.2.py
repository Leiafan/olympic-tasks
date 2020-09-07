

def gcd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

d1 = 10**len(str(c))
d2 = 10**(len(str(c))**2)
c1 = c*d1//(d1-1)

p_q = a + b/d1 + c/((d1-1)*d2)
q = 1
p = q * p_q
q = p_q / p
d = gcd(int(p), int(q))
p /= d
q /= d


print(int(p), '/', int(q))
