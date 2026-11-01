# To implement Best First Search using a heuristic value to find the goal element in a list.
n = int(input("Enter number of elements: "))

lst = []
h = []

for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

for i in range(n):
    x = int(input("Enter heuristic value: "))
    h.append(x)

goal = int(input("Enter goal element: "))

visited = []

while len(visited) < n:
    best = -1
    min_h = 999

    for i in range(n):
        if lst[i] not in visited and h[i] < min_h:
            min_h = h[i]
            best = i

    if best == -1:
        break

    current = lst[best]
    visited.append(current)

    print("Selected:", current, "Heuristic:", h[best])

    if current == goal:
        print("Goal found!")
        break

else:
    print("Goal not found!")
