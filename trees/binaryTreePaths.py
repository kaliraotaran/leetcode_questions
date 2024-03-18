'''
https://leetcode.com/problems/binary-tree-paths/submissions/1207528717/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def solve(root, s):
            s+= str(root.val)
            if not root.right and not root.left:
                ans.append(s)
                return 
            if root.right:
                solve(root.right, s+'->')
            if root.left:
                solve(root.left, s+'->')
        solve(root, '')
        return ans