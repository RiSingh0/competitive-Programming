t=int(input())
for _ in range(t):
    n=int(input())
    mat=[[int(x) for x in input().split()] for i in range(n)]
    if mat[0][1] == 2:
        fixed=True
        count=0
    else:
        fixed=False
        count=1
    for i in range(2,n):
        if mat[0][i] != i+1:
            if fixed:
                count+=2
            fixed=False
        else:
            fixed=True
    print(count)
                
                