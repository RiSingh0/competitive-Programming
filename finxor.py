def modifyBit( n,  p,  b): 
    mask = 1 << p 
    return (n & ~mask) | ((b << p) & mask) 
    
t=int(input())
for _ in range(t):
    n=int(input())
    num=1
    for i in range(19):
        num=num<<1
        num=num|1
    print("1",num)
    x=int(input())
    ans=0
    ans0=0
    for i in range(19):
        num1=modifyBit(num,i,0)
        print("1",num1)
        y=int(input())
        t=x+y
        ind=1<<i
        t-=(ind*n)
        t//=2
        diff=y-t
        if (diff//ind)%2 != 0:
            ans+=ind
        diff=x-t
        ans0+=diff
    x=x-ans0
    ind=1<<19
    t=(ind*n)
    t-=x
    if (t//ind)%2 != 0:
        ans+=ind
    print("2",ans)
    b=int(input())
    if b == -1:
        exit()
        
        