def fibo(n):
	if n == 1:
		return 1;
	elif n == 2:
		return 1;
	
	return fibo(n-1) + fibo(n-2);

n = int(input("Entre com um numero maior ou igual que 1 \n"));
print("O numero de fibonnaci que voce digitou eh: " + str(fibo(n)));