N, X = ((input()).split())  #Numero de valvulas
taps = ((input()).split())  #Valor das valvulas

N = int(N)
X = int(X)

maior = False
menor = False
igual = False

for x in taps:
    v = int(x)
    if X == v:
        igual = True
    elif v > X:
        maior = True
    elif v < X:
        menor = True
       
if igual:
    print(1)
elif maior and menor:
    print(2)
else:
    print(-1)
     
