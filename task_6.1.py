# Convert an ordinary fraction p / q to a decimal periodic fraction A, B (C). p, q -
# natural numbers in the range [1; 10000] in decimal notation p = int(input("p = "))
q = int(input("q = "))


def base(nominator, denominator, maxlen=20):
    signstr = ""
    if nominator < 0:
        signstr = "-"
    num = abs(nominator)
    den = denominator
    xint = num / den
    num = num % den
    zerosbase = 1
    zeroslen = 0
    while den % 2 == 0 or den % 5 == 0:
        if den % 2 == 0:
            den /= 2
        if den % 5 == 0:
            den /= 5
        zerosbase *= 10
        zeroslen += 1
    ninesbase = 0
    ninesbaselen = 0
    r = zerosbase

    while r % den and ninesbaselen < maxlen:
        ninesbase = ninesbase * 10 + 9
        ninesbaselen += 1
        r = ninesbase * zerosbase
    pstr = ""
    npstr = ""
    if ninesbase > 0:
        x = num * ninesbase * zerosbase / denominator
        xnp = x / ninesbase
        xp = x % ninesbase
        tail = ""
        if r % den:
            tail = ".."
        pstr = ("(%0" + str(ninesbaselen) + "d%s)") % (xp, tail)
    else:
        xnp = num * zerosbase / denominator
    if zeroslen > 0:
        npstr = ("%0" + str(zeroslen) + "d") % (xnp)

    s = signstr + "%d" % (xint)
    if ninesbase > 0 or zeroslen > 0:
        s += "." + npstr + pstr

    return s


print(base(p, q))
