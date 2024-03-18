'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        while stack or root: # enters a loop until both the stack and root are empty
            if root: #checks if the root exits
                stack.append(root) # adds the root to the stack(the whole root node juyst the value of teh root)
                root = root.left #moves to teh left child of the root
            else:  #this executes when the root is None (means it reached teh leftmost node)
                node = stack.pop() # pops the top node from the stack(it was the root node that we added in the above if statement)
                res.append(node.val) # this adds the value of the curretn node to the result list
                root = node.right # moves to teh right child of the popped node
        return res # this will print the resultant inorder traversed list
    


# recursive on codeing ninja
    
'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''

def inorder(root, answer):
    if root == None:
        return 
    inorder(root.left, answer)
    answer.append(root.data)
    inorder(root.right, answer)

def getInOrderTraversal(root):
    # Write your code here.
    answer = []
    inorder(root, answer)
    return answer

    
    