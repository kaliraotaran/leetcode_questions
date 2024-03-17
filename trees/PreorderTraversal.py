

'''
https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1206305199/
''' 

class TreeNode:
    def __init__(self, val , left, right) -> None:
        self.val= val 
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return res