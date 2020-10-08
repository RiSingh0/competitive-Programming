def power(x, y): 
    res = 1
    while (y > 0): 
        if ((y & 1) == 1) : 
            res = res * x 
        y = y >> 1
        x = x * x 
    return res 
k=int(input())
if k == 4:
    arr=[power(int(x)+1,k) for x in range(64)]
    set1=set()
    set1.add(0)
    for i in range(20):
        num=arr[i]
        set2=set()
        set2.add(num)
        for each in set1:
            set2.add(num+each)
        set1.update(set2)
    # #print(*set1)
    # #exit()
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr1=arr[:n]
        print(arr1)
        mid=sum(arr1)
        print(mid)
        mid//=2
        ans=[]
        count=0
        #print(set1)
        mid-=6
        #print(arr1)
        print(mid)
        for i in range(n-1,-1,-1):
            count+=arr[i]
            #print(count)
            if (count <= mid) and (mid-count in set1):
                ans.append("1")
            else:
                count-=arr[i]
                ans.append("0")
        ans.reverse()
        val=0
        for i,each in enumerate(ans):
            if each == "1":
                val+=arr1[i]
            print(each,end="")
        print()
        print(val)
