'''
https://www.codingninjas.com/studio/problems/find-minimum-number-of-coins_975277?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION

'''

from typing import List

def MinimumCoins(n: int) -> List[int]:
    # write your code here
    listt = [1000,500,100,50,20,10,5,2,1]
    list2 = []
    i=0
    while i < len(listt):
        if listt[i]>n:
            i+=1
        else:
            list2.append(listt[i])
            n -= listt[i]

    return list2


