print("Hello world")

def fibo(a):
    if a == 0:
        return 1
    return fibo(a-1) + fibo(a-2)

fibo(100)