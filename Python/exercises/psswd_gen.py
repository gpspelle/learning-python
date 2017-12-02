import string
import random

def build_strong():
    passwd = []
    for i in range(12):
        rand = random.randrange(3)
        if rand == 0:
            passwd.append(random.choice(string.ascii_lowercase))
        elif rand == 1:
            passwd.append(str(random.randrange(10)))
        else:
            passwd.append(random.choice(string.ascii_uppercase)) 
    return passwd

def build_medium():
    passwd = []
    for i in range(8):
        rand = random.randrange(2) 
        if rand % 2 == 0:
            passwd.append(random.choice(string.ascii_lowercase))
        else:
            passwd.append(str(random.randrange(10)))
    return passwd

def build_weak():
    passwd = []
    for i in range(6):
        passwd.append(str(random.randrange(10)))

    return passwd

print("PASSWORD GENERATOR")
while True:
    how_strong =  raw_input("How strong you want your password? Strong, Medium or Weak?\n")
    if how_strong == "Strong" or how_strong == "strong":
        passwd = build_strong()
        break
    elif how_strong == "Medium" or how_strong == "medium":
        passwd = build_medium()
        break
    elif how_strong == "Weak" or how_strong == "weak":
        passwd = build_weak()
        break
    else:
        print("You have entered a invalid strongness, please enter: Strong, Medium or Weak") 
        print("Try again...")

passwd = (''.join(passwd))
print("Your password: " + (passwd))
