import math

def split(arr, count):
         return [arr[i::count] for i in range(count)]

n = int(input())

for x in range(0, n):
    small = input()
    small = int(small)
    aux = small
    sum_of_digits = 0 
    while aux >= 10:
        print(sum_of_digits)
        sum_of_digits += int((aux % 10))
        aux = aux / 10

    sum_of_digits += int(aux) 
    print(sum_of_digits)
    break
    while small <= 1000000000:
        if small % 2 == 0:
            small += 1
            continue
        aux = small
        divisors = []
        for y in range(2, int(math.sqrt(small))):
            print(y)
            if aux % y == 0:
                divisors.append(y)
                
        #print(divisors)
        for t in divisors:
            while t > 10:
                divisors.append(t/10)
                t = t % 10
                
        #print(divisors)
        sum_of_divisors = 0
        for t in divisors:
            if t < 10:
                sum_of_divisors += int(t)
       
        if sum_of_digits == sum_of_divisors:
            #print(small)
            break

        small += 1
