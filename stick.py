t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    set1=set(arr)
    if 0 in set1:
        print(len(set1)-1)
    else:
        print(len(set1))