

'''
https://leetcode.com/problems/path-sum/submissions/1242703838/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, cursum):
            if node is None:
                return False
            cursum += node.val
            if not node.left and not node.right:
                return cursum == targetSum
            return helper(node.left, cursum) or helper(node.right, cursum)
        if not root:
            return None
        return helper(root, 0)