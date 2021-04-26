print("Hello world")
a,b = 0,0
for i in range(100):
    a,b = b, a+b
    print(a)