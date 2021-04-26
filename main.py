print("Hello world")

def fibo(a):
    if a <= 1:
        return 1
    return fibo(a-1) + fibo(a-2)

print(fibo(10))