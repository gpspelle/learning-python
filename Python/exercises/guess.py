import random

val = random.randint(1, 9)
attempts = 0

while True:

	guess = input("Enter a number between 1 and 9. Or 'exit' to leave\n")

	if guess == "exit":
		break;

	attempts += 1 

	try:	
		guess = int(guess)
	except TypeError:
		print("Incorrect input... exitting")
		break;

	if guess == val:
		print("You guessed the randomly sorted number!")
		print("Number of attempts: " + str(attempts))
		break;

	elif guess > val:
		print("You guessed a higher number than the sorted one!")
	
	else:
		print("You guessed a smaller number than the sorted one!")
	 
	
