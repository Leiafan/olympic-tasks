

def last_dig(x):
    result = 1
    for i in range(2, x+1):
        j = i
#        while j % 2 == 0:
#            j //= 2
#        while j % 5 == 0:
#            j //= 5
        while j % 10 == 0:
            j //= 10
        result = result*j
    return result % 10


n = int(input("n  = "))

print(str(last_dig(n)))
