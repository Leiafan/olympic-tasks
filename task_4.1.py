# A rectangle drawn on checkered paper with dimensions M * N has a diagonal cut.
# Determine the number of cells that this diagonal intersects, M and N - natural numbers which belongs [1; 10000]
 

def intersection_amount(x, y):
    temp_x = x
    temp_y = y
    while x != 0 and y != 0:
        if x > y:
            x -= y
        else:
            y -= x
    return temp_x + temp_y - x - 1


m = int(input("m = "))
n = int(input("n = "))
print("X =", intersection_amount(m, n))
