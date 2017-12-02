import random
a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
c = []
d = []

# hey, cool stuff
for elemA in a:	
	if elemA in b:
		if elemA not in c:
			c.append(elemA)	
			

# hey, let me fuck your brain
d = [i for i in a if i in b]

print(c)
print(d)
		
