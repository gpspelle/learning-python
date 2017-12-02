print("Enter a integer")
number = int(input())

if number % 4 == 0:
    print("The number " + str(number) + " is multiple of 4")
elif number % 2 == 0:
    print("The number " + str(number) + " is odd!")
else:
    print("The number " + str(number) + " is even!")

