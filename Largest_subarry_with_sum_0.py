def maxLen(n, arr):
    dic, add, L, R = {}, 0, -1, -1
    for i in range(len(arr)):
        if add not in dic:
            dic[add]=i
        add+=arr[i]
        if add in dic:
            if R-L < i-dic[add]:
                L=dic[add]
                R=i
    val=(R-L)
    if L != -1:
        val+=1
    return val
