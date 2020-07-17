def binpow(a,b):
    res=1
    while b > 0 :
        #print(res,a,b)
        if b & 1 :res = res * a
        a *= a
        b >>= 1
    return res

print(binpow(2,2))
        
