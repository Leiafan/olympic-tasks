# Find the number of zeroes,which ends decimal digit n!
# Find the last digit n!, which not equals zero



def check(x):
    result = 0
    while x > 0:
        x //= 5
        result += x
    return result


n = int(input("n  = "))

print(str(check(n)))
