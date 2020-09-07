# Given triangle with dimensions AxB where A, B are natural numbers. Create a partitioning program of this rectangle by the smallest possible number of squares 

a = int(input("A = "))
b = int(input("B = "))


def greatest_squares(x, y):
    while x != 0 and y != 0:
        if x > y:
            print(y, " ", y)
            x -= y
        else:
            print(x, " ", x)
            y -= x


greatest_squares(a, b)
