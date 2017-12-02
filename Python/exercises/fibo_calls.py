calls = 0

def increase_calls():
    global calls
    calls += 1

def set_calls(n):
    global calls
    calls = n

def fibo(n):

    increase_calls()

    if n < 2: 
        return n 
    else: 
        return fibo(n-1) + fibo(n-2)

cases = int(input())
for i in range(0, cases):
    n = int(input())
    set_calls(0)
    n_fibo = fibo(n)
    
    if n > 1:
        calls = calls - 1

    print("fib(" + str(n) + ") = " + str(calls) + " calls = " + str(n_fibo))
