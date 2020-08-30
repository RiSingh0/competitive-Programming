n=int(input())
arr=[int(x) for x in input().split()]
if n < 2:
    if n == 1:
        print("1",n)
        print(-1*arr[0])
        print("1",n)
        print(0)
        print("1",n)
        print(0)
    else:
        print("1 1")
        print(-1*arr[0])
        print("2 2")
        print(-1*arr[1])
        print("1 1")
        print("0")
        
else:
    print("1",n-1)
    for i in range(n-1):
        k=arr[i]%(n)
        arr[i]+=(k*(n-1))
        print(k*(n-1),end=" ")
    
    print()
    print("2",n)
    for i in range(1,n):
        k=arr[i]%(n)
        arr[i]+=(k*(n-1))
        print(k*(n-1),end=" ")
    print()
    print("1",n)
    for i in range(n):
        print(-1*arr[i],end=" ")
    print()
    