'''
https://www.naukri.com/code360/problems/k-most-frequent-elements_3167808?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=DISCUSS
'''

from typing import List

def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    hash = {}

    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            if i in hash:
                hash[i] +=1
    a = sorted(hash.keys(), key = lambda x:(-hash[x], -x))
    return a[:k]