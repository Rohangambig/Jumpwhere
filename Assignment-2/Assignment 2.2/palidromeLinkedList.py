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
    
    def isPalindrome(self):
        prev = None

        current_node = self.head
        while current_node:
            new_node = Node(current_node.data)
            new_node.next =  prev
            prev = new_node
            current_node =  current_node.next
        
        current_node1 = prev
        current_node2 =  self.head

        while current_node1:
            if current_node1.data != current_node2.data:
                return False
            current_node1 = current_node1.next
            current_node2 = current_node2.next
            
        return True


L = LinkedList()
arr = [1,2,3,4,5]

for num in arr:
    L.addelement(num)

L.displayNodes()
print()
print("Palidrome or not : ",L.isPalindrome())

