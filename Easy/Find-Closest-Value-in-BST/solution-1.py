class BST:
    def __init__(self, data=None):
        self.right = None
        self.left = None
        self.data = data
    
    # Insert method to create BST Nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            
            elif data > self.data:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.data)

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.data):
            closest = currentNode.data
        if target < currentNode.data:
            currentNode = currentNode.left
        elif target > currentNode.data:
            currentNode = currentNode.right
        else:
            break
    return closest

bst = BST(23)

bst.insert(12)
bst.insert(9)
bst.insert(27)
bst.insert(24)
bst.insert(11)
bst.insert(80)


print(findClosestValueInBst(bst, 72))

