
'''
https://www.codingninjas.com/studio/problems/unique-element-in-sorted-array_1112654?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''
def singleNonDuplicate(arr):
    # Write your code here
    hash1= {}

    for c in arr:
        if c not in hash1:
            hash1[c] =1
        else:
            if c in hash1:
                hash1[c]+=1
    for key, values in hash1.items():
        if values ==1:
            return key


