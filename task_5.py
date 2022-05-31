# Rectangle with sides A and B given. Some smaller rectangles will be erased.
# Find the new dimensions of the possible rectangle.

a = int(input("A = "))
b = int(input("B = "))
amount = int(input("N = "))
Xi = []
Yi = []

for i in range(amount):
    x = int(input("X["+str(i+1)+"] = "))
    Xi.append(x)
    y = int(input("Y["+str(i+1)+"] = "))
    Yi.append(y)

ab = [Xi[i] * Yi[i] for i in range(amount)]

current_area = 0
for i in range(amount):
    current_area += ab[i]

removed_area = a * b - current_area
x_sum = 0

for i in range(amount):
    x_sum += Xi[i]

sl = x_sum // a + 1
w = sl * a - x_sum
h = removed_area // w

print("W =", w)
print("H =", h)
