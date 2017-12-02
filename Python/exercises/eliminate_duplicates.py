def remove_duplicates(lis):
    new_lis = []
    for i in range(0, len(lis)-1):
        if lis[i] not in new_lis:
            new_lis.append(lis[i]) 
        lis[i] = -1 
    return new_lis

lis = [1, 1, 2, 2, 3, 3]
new_lis = remove_duplicates(lis)
print new_lis
