while True:
    N, M = (input().split())
    
    N = int(N)
    M = int(M)
    if N == 0 and M == 0:
        break
   
    mat = []
    for x in range (0, N):
        vet = []
        for y in range(0, M):
            vet = input().split()
            yet = []
            for k in vet:
                yet.append(int(k))

        mat.append(yet)
   
    best = 0
    for x in range (1, N+1):
        for y in range(1, M+1):
            zeros = x*y
            keep = True
            while keep:
                for k in range(0, N):
                    if keep == False:
                        break
                    for j in range(0, M):
                        if keep == False:
                            break
                        if mat[k][j] == 1:
                            keep = False 
                        else:
                            zeros -= 1
            if zeros == 0 and x*y >= best:
                best = x*y
    print(best)
                
     
