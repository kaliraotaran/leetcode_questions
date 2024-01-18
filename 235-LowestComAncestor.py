# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val>curr.val and q.val >curr.val:
                curr = curr.right
            elif q.val <curr.val and p.val <curr.val:
                curr= curr.left
            else:
                return curr
            