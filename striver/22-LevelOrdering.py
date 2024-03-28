'''
https://www.naukri.com/code360/problems/level-order-traversal_796002?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''


from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)


#   Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def getLevelOrder(root):

    #   Write your code here
    ans = []
    q = []

    q.append(root)
    while len(q)>0:
        temp = q[0]
        q.pop(0)
        if temp:
            ans.append(temp.val)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
    return ans





























#   Fast input
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root


def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# main
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getLevelOrder(root)
    printAns(ans)
