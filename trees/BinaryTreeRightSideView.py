

'''
https://leetcode.com/problems/binary-tree-right-side-view/submissions/1247924793/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we're gonna use BFS and for each level we want the right most values
            # of the tree
            res = []
            q = collections.deque([root])
            while q:  #while there even is an element in the queue
                rightSide = None    
                qLen = len(q)   

                for i in range(qLen): 

                    node = q.popleft()  # we poped the first node of the queue
                    if node :
                        rightSide = node  
                        q.append(node.left)  
                        q.append(node.right)
                if rightSide:
                    res.append(rightSide.val)
            return res
