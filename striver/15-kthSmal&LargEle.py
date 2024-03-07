'''
https://www.codingninjas.com/studio/problems/kth-smallest-and-largest-element-of-array_1115488?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''

def kthSmallLarge(arr, n,k):
    arr.sort()
    return arr[k-1], arr[n-k]