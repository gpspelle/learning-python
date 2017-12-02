number = int(input("Enter a number: "))
possible = range(1, number+1)
divisors = []
for i in possible:
    if number % i == 0:
        divisors.append(i)

print("Positive divisors of " + str(number))
for i in divisors:
    print(i)
