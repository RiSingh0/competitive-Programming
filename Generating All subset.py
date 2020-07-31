def subset(arr,li,n,ind):
    print(*li)
    for i in range(ind, n):
        li.append(arr[i])
        subset(arr,li,n,i+1)
        li.pop()
    return 

n=int(input())
arr=[int(x) for x in input().split()]
subset(arr,[],n,0)
