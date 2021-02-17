class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    # Insert method to create nodes
    def insert(self, data):
        
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    # find the val to compare the value with nodes
    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + " not found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + " not found"
            return self.right.findval(val)
        else:
            print(str(self.data) + " is found")
    
    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
            

root = Node(12)  
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(1)
root.insert(15)

# print(root.findval(7))
# print(root.findval(14))

print(root.right.left)
# root.PrintTree()
           
