# first we do general tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level =0
        p = self.parent
        while p:
            level+=1
            p = self.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() *3 # defing the prefix level spacings
        print(f"{spaces}" + self.data)
        if self.children:
            for child in self.children:
                child.print_tree() # it'll recursively call this function and print all nodes of tree



def electronics_tree():
    root = TreeNode("Electronics")

    computer= TreeNode('Computer')
    computer.add_child(TreeNode('Mac'))
    computer.add_child(TreeNode('Microsoft Surface'))

    phones = TreeNode('Phones')
    phones.add_child(TreeNode('Iphones'))
    phones.add_child(TreeNode('Samsung'))
    phones.add_child(TreeNode('Google Pixel'))

    tv = TreeNode('Tv')
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Samsung'))

    root.add_child(computer)
    root.add_child(phones)
    root.add_child(tv)

    return root

tree = electronics_tree()
# tree.print_tree()


# -- BRINARY TREE --
# its a regular tree with the constraint that it has at most 2 children
# traversal techq. BFS and DFS ( we onyl did DFS inorder techq. here)
# binary tree cant have duplicate value
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return # since a bianry tree cant have duplicate value
        
        if data<self.data:
            # add to left side of tree
            if self.left: # if there is already a node at the left recursively allocated the node
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        else:
             # add to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
    def in_order_traversal(self):
        elements = []
            # visit the left tree first
        if self.left:
            elements += self.left.in_order_traversal() # it will keep going left until there isn't any
            # visit the base node
        elements.append(self.data)
            # visit the right tree last
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # the value MIGHT be in the left side of the tree
            if self.left:
                return self.left.search(val)
            else:
                return False # reached end and the val doesnt exist
            
        if val> self.data:
            # then the value MIGHT be on the right side of the tree
            if self.right:
                return self.right.search(val)
            else:
                return False
    def maximum(self):
        if self.right == None:
            return self.data
        return self.right.maximum()

    def minimum(self):
        if self.left ==None:
            return self.data
        return self.left.minimum()

    def delete(self, val):
        if val<self.data:
            if self.left:
               self.left =  self.left.delete(val)
            else:
                return None
        elif val >self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                return None
        else:
            if self.left == None and self.right == None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            minval = self.right.minimum()
            self.data= minval
            self.right = self.right.delete(minval)
        return self

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

num =[17,4,1,20,9,23,18,34]
numberstree = build_tree(num)
print("In order traversal : ", numberstree.in_order_traversal())
print(numberstree.search(17))
print(numberstree.delete(20))
print(numberstree.in_order_traversal())