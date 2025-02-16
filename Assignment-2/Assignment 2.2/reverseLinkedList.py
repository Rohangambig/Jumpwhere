class Node:
    def __init__(self,data = None):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def addelement(self,data):
        if self.head is None:
            self.head = Node(data)
            return 

        new_node = Node(data)
        current_node = self.head 

        while current_node.next:
            current_node = current_node.next 
        
        current_node.next = new_node
        return 
    
    def displayNodes(self):
        current_node = self.head 
        while current_node:
            print(current_node.data,end= " ")
            current_node = current_node.next 
        
    def reverseList(self):
        
        
        current_node = None

        node = self.head
        while node:
            new_node = Node(node.data)
            new_node.next = current_node
            current_node = new_node
            node = node.next
        
        return current_node

L = LinkedList()
arr = [1,2,3,4,5]

for num in arr:
    L.addelement(num)

L.displayNodes()
L.reverseList()
print()
L.displayNodes()
