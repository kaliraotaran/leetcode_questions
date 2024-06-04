

'''
https://leetcode.com/problems/merge-intervals/submissions/1277754528/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        res = []

        i = 0 

        for j in intervals:
            if len(res) ==0:
                res.append(j)
            else:
                if res[i][1]> j[1]:
                    continue
                elif res[i][1] >= j[0]:
                    res[i][1]= j[1]
                else:
                    res.append(j)
                    i+=1
        return res
        