class Node:
    def __init__(self,data):
        self.data = data
        self.left  =  self.right = None

class Tree:
    def addNodes(self,root,data):
        new_node = Node(data)
        current_node = root 

        if current_node == None: return new_node

        while current_node:
            if data > current_node.data:
                if current_node.right is None:
                    current_node.right = new_node ; break 
                else:
                    current_node = current_node.right 

            elif data < current_node.data: 
                if current_node.left is None: 
                    current_node.left = new_node;break
                else:
                    current_node = current_node.left 
        
        return root 


    def Inorder(self,root):
        if root:
            self.Inorder(root.left)
            print(root.data,end=" ")
            self.Inorder(root.right)
    

    def checkSymmetric(self,root1,root2):
        if root1 is None and root2 is None: return True 
        if root1.data != root2.data: return False 

        return self.checkSymmetric(root1.left,root2.right) and self.checkSymmetric(root1.right,root2.left) 

    def is_symmetric(self,root):
        if not root: return True 
        return self.checkSymmetric(root.left,root.right)

T = Tree()

root = T.addNodes(None,5)
root = T.addNodes(root,6)
root = T.addNodes(root,3)
root = T.addNodes(root,8)
root = T.addNodes(root,2)
root = T.addNodes(root,1)
root = T.addNodes(root,7)
root = T.addNodes(root,10)

T.Inorder(root)
print(T.is_symmetric(root))
