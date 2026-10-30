# water jug prblm

a = int(input("Enter capacity of jug A: "))
b = int(input("Enter capacity of jug B: "))

x = 0
y = 0

goal = int(input("Enter goal amount: "))

print("Initial State:", x, y)

while x != goal and y != goal:

    if x == 0:
        x = a
        print("Fill jug A:", x, y)

    elif y == b:
        y = 0
        print("Empty jug B:", x, y)

    else:
        t = min(x, b - y)
        x = x - t
        y = y + t
        print("Pour A into B:", x, y)

print("Goal Reached:", x, y)
