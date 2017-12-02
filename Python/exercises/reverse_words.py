words = input("Enter some words, like 4 or 5\n")
reverse = words.split()

for i in range(len(reverse)):
    if i == len(reverse)-1:
        print(reverse[0], "", end="\n")
    else:
        print(reverse[len(reverse)-i-1], " ", end="")
