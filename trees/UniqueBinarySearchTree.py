
'''
https://leetcode.com/problems/unique-binary-search-trees/submissions/1246750751/
'''


class Solution:
    def numTrees(self, n: int) -> int:
        
        numTrees = [1] *(n+1)
        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root - 1
                right = nodeAs - root
                total += numTrees[left] * numTrees[right]
            numTrees[nodes] = total
        return numTrees[n]