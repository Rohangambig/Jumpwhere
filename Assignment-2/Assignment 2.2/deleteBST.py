# This program is also an example of inserting the new node into the BST

class Node:
    def __init__(self,data= None):
        self.data = data 
        self.left =  self.right = None 

class Tree:
    def addNodes(self,root,data):
        if not root:
            root = Node(data)
            return root 

        new_node = Node(data)
        current_node =  root 
        while current_node:
            if data > current_node.data:
                if current_node.right is None: current_node.right = new_node ;break
                else: current_node =  current_node.right
            
            else:
                if current_node.left is None: current_node.left = new_node; break
                else: current_node = current_node.left 
        
        return root 

    def Display(self,root):
        if root:
            self.Display(root.left)
            print(root.data,end=" ")
            self.Display(root.right)
    
    def DeletingNode(self,root,key):
        if not root: return None
        elif root.data == key:
            if not root.left and not root.right: return None 
            elif not root.left and root.right: return root.right
            elif not root.right and root.left: return root.left 

            ptr = root.right
            while ptr.left: ptr = ptr.left 
            root.data =  ptr.val
            root.right = self.DeletingNode(root.right,root.val)            

        elif root.data > key:
            root.left = self.DeletingNode(root.left,key)
        else:
            root.right = self.DeletingNode(root.right,key)
        
        return root
        

T = Tree()
root = T.addNodes(None,5)
root = T.addNodes(root,2)
root = T.addNodes(root,1)
root = T.addNodes(root,3)
root = T.addNodes(root,4)
root = T.addNodes(root,6)
T.Display(root)
print()

root = T.DeletingNode(root,3)
print("\nAfter deleting the node : ")
T.Display(root)
