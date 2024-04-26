

'''
https://leetcode.com/problems/count-complete-tree-nodes/submissions/1242710164/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node= stack.pop()
                res.append(node.val)
                root= node.right
        return len(res)