for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    maxa=0
    count=0
    for i in range(n):
        if arr[i] == 0:
            count+=1
        else:
            if count > maxa:
                maxa=count
            count=0
    chk=0
    count=0
    for i in range(n):
        if arr[i] == 0:
            count+=1
        else:
            if count > maxa//2:
                chk+=1
            count=0
            
    if chk < 2:
        if maxa%2 == 0:
            print("No")
        else:
            print("Yes")
    else:
        print("No")