'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d =0 
        if not root:
            return d
        q = [root]
        while q:
            ns = []
            while q:
                ns.append(q.pop())
            while ns:
                n =ns.pop()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            d+=1
        return d
    
'''
method 2- here we use recursion where we recursively go to left or right of tree and add 1 to the answer
and in the end it will return the answer
'''