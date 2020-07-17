def mergeSort(arr,l,r,ind,count):
    if l < r:
        #middle of array
        mid=(l+r)//2
        
        #recursion both side
        mergeSort(arr,l,mid,ind,count)
        mergeSort(arr,mid+1,r,ind,count)
        #initialize variable
        start=l
        l1=mid+1
        li=[]
        cnt=0
        #Take the smallest
        while l <= mid and l1 <= r:
            if arr[ind[l]] <= arr[ind[l1]]:
                li.append(ind[l])
                count[ind[l]]+=cnt
                l+=1
            else:
                li.append(ind[l1])
                cnt+=1
                l1+=1
                
        #Take the LeftOver
        if l1 > r:
            while l <= mid:
                li.append(ind[l])
                count[ind[l]]+=cnt
                l+=1
                
        #Take the LeftOver
        if l > mid:
            while l1 <= r:
                li.append(ind[l1])
                l1+=1
                
        #changing in index track
        for i in range(start,r+1):
            ind[i]=li[i-start]

arr=[3, 4, 2, 1, 1, 2 ,5 , 3]
#To Track the index
ind=[i for i in range(len(arr))]
#To Track the Count
count=[0 for i in range(len(arr))]
#sort
mergeSort(arr.copy(),0,len(arr)-1,ind,count)
print("My array :",arr)
print("Count    :",count)
