def Help(arr):
    #initialize
    Longest_seq = 0
    #arr to setConversion
    arr_set = set(arr)
    #iterate to each
    for each in arr_set:
        #Don't  go if you already
        if each - 1 not in arr_set:
            #initialize
            running_num = each
            running_seq = 1
            #check running seq
            while running_num + 1 in arr_set:
                running_num += 1
                running_seq += 1
            #replace if required
            Longest_seq = max(Longest_seq, running_seq)
    return Longest_seq

#array with values
arr=[1,2,4,5,7,8,9]
print(Help(arr))
