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

    
    def KthSmallestEle(self,root,k):
        arr = []

        def Helper(root,arr):
            if root: 
                Helper(root.left,arr)
                arr.append(root.data)
                Helper(root.right,arr)
        
        Helper(root,arr)
        return arr[k-1]

T = Tree()
root = T.addNodes(None,5)
root = T.addNodes(root,4)
root = T.addNodes(root,8)
root = T.addNodes(root,1)
root = T.addNodes(root,3)
T.Display(root)
print()

print("\nKth Smallest Element is : ",T.KthSmallestEle(root,2))