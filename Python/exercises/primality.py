number = int(input("Enter a number: \n"))
divisors = 0
for i in range(1, number+1):
    if number % i == 0:
        divisors += 1

if divisors != 2: 
    print("The entered number inst prime")
else:
    print("The enterd number is prime")
