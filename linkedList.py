class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def size(self):
        print('this is the length: {length}'.format(length = self.length))
    
    def currentHead(self):
        print(self.head)
        print('this is the head: {head}'.format(head=self.head))
    
    def insertElement(self, element):
        node = Node(element)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        
        self.length += 1
        print('the element is added to the end of the linked list')
    
    def removeElement(self, element):
        current = self.head
        if current.item == element:
            self.head = current.next
        else:
            while current.item != element:
                previous = current
                current = current.next
            previous.next = current.next
        self.length -= 1
        print('{element} is removed'.format(element=element))
    
    def printTheList(self):
        while self.head != None:
            print(self.head.item)
            self.head = self.head.next

linkedList = LinkedList()
linkedList.insertElement(1)
linkedList.insertElement(2)
linkedList.insertElement(3)
linkedList.insertElement(4)
linkedList.insertElement(5)

# linkedList.removeElement(3)
# linkedList.removeElement(5)
# linkedList.insertElement(5)
linkedList.printTheList()
linkedList.size()
print(linkedList.head)
# linkedList.currentHead()



    