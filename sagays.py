
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
arr1=arr[0:n//2]
arr2=arr[n//2:]
arr3=[]

for i in range(n//2):
    arr3.append(arr2[i])
    arr3.append(arr1[i])
if n%2 != 0:
    arr3.append(arr2[-1])

cnt=0
for i in range(1,n-1):
    if arr3[i-1] > arr3[i] < arr3[i+1]:
        cnt+=1
print(cnt)
print(*arr3)
    
    
    
    
    