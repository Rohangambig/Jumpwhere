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

    def maxDepth(self,root):
        if not root:
            return 0 
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

T = Tree()
root = T.addNodes(None,5)
root = T.addNodes(root,2)
root = T.addNodes(root,1)
root = T.addNodes(root,6)
T.Display(root)
print()


print("Minimum depth of a binary tree : ",T.maxDepth(root))