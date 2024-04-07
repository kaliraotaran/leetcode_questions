
'''
https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        maxindex = len(citations)
        for i in citations:
            if i < maxindex:
                maxindex-=1
        return maxindex
