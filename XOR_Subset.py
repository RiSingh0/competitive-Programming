from math import log2,ceil
def subset(arr,target):
    maxa=max(arr)
    n=len(arr)
    m=(1<<ceil(log2(maxa))+1)-1
    if target > m:
        return 0
    dp=[[0 for _ in range(m+1)] for x in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(m+1):
            dp[i][j]=dp[i-1][j]+dp[i-1][j^arr[i-1]]
    #print(dp)
    return dp[i][target]
    
t=int(input())
for _ in range(t):
    n,target=map(int,input().split())
    arr=[int(x) for x in input().split()]
    print(subset(arr,target))
