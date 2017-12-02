import random

l1 = random.sample(range(7), 4)
l2 = random.sample(range(7), 4)

common = []

print("Random list 1: ", l1)
print("Random list 2: ", l2)

for i in l1:
    for j in l2:
        if i == j:
            common.append(i) 

if len(common) == 0:
    print("The list of common elements is empty!")
else:
    print("The list of common elements is: ", common)
