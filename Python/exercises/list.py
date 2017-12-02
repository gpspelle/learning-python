old = [1, 2, 3, 4, 5, -1, -2]
new = []

limit = int(input("Enter a limit value for your list: "))
for i in old:
    if i > limit:
        new.append(i)

for i in new:
    print("My list have " + str(i))
