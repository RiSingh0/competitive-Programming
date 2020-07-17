def GCD(a,b):
    while b:
        a %= b
        a ,b = b, a
    return a

print(GCD(20,10))
