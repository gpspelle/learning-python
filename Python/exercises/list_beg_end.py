import random

def get_first(lis):
    return lis[0]
def get_last(lis):
    return lis[len(lis)-1]

lis = random.sample(range(10), 5)
print lis

end_begin = [get_first(lis), get_last(lis)]
print end_begin
