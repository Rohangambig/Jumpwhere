from collections import deque
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
        
    def balanceBST(self,root):
        cur_node = root 
        def storeArr(root,arr):
            if root:
                storeArr(root.left,arr)
                arr.append(root.data)
                storeArr(root.right,arr)
        
        arr = []
        storeArr(cur_node,arr)
        arr.sort()

        def Helper(l,r):
            if l > r: return

            m = (l + r) // 2 
            root = Node(arr[m])
            root.left = Helper(l,m-1)
            root.right = Helper(m+1,r)
            return root

        return Helper(0,len(arr)-1)
     
T1 = Tree()
root1 = T1.addNodes(None,4)
root1 = T1.addNodes(root1,3)
root1 = T1.addNodes(root1,2)
root1 = T1.addNodes(root1,1)
T1.Display(root1)

print("\nAfter balancing the binary search tree ",end=" ")
root = T1.balanceBST(root1)
T1.Display(root)
