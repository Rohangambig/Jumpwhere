class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def addelement(self, data):
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
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    

    def mergeTwoLists(list1, list2):
        head1 = list1.head
        head2 = list2.head
        dummy_node = current_node = Node()

        while head1 and head2:
            if head1.data > head2.data:
                current_node.next = Node(head2.data)
                head2 = head2.next
            else:
                current_node.next = Node(head1.data)
                head1 = head1.next

            current_node = current_node.next

        while head1:
            current_node.next = Node(head1.data)
            head1 = head1.next
            current_node = current_node.next

        while head2:
            current_node.next = Node(head2.data)
            head2 = head2.next
            current_node = current_node.next
        
        merged_list = LinkedList()
        merged_list.head = dummy_node.next
        return merged_list  


L1 = LinkedList()
arr1 = [1, 3, 5, 7]

for num in arr1:
    L1.addelement(num)

L2 = LinkedList()
arr2 = [2, 4, 6, 8]

for num in arr2:
    L2.addelement(num)

print("List 1:")
L1.displayNodes()
print("List 2:")
L2.displayNodes()

merged = LinkedList.mergeTwoLists(L1, L2)
print("Merged List:")
merged.displayNodes()

