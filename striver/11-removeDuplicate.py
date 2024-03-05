
'''
https://www.codingninjas.com/studio/problems/remove-duplicates-from-sorted-array_1102307?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''


def removeDuplicates(arr,n):
    # Write your code here.
    hash1 = {}

    for i in arr:
        if i not in hash1:
            hash1[i] = 1
        else:
            if i in hash1:
                hash1[i]+=1
    
    length =0 
    for keys in hash1.keys():
        length +=1
    return length
