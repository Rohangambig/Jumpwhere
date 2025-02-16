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

    def levelOrder(self,root):
        if not root: return []
        q = deque()
        q.append(root)
        output = [] 

        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()

                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                level.append(cur.data)
            
            output.append(level)
        return output
    
    def sameTree(self,root1,root2):
        if not root1 and not root2: return True 
        elif (not root1 and root2) or (not root2 and root1) or root1.data !=  root2.data: return False 
        return self.sameTree(root1.left,root2.left) and self.sameTree(root1.right,root2.right)

T1 = Tree()
root1 = T1.addNodes(None,2)
root1 = T1.addNodes(root1,1)
root1 = T1.addNodes(root1,3)
print("Level order Tree 1 : ",T1.levelOrder(root1))
print()

T2 = Tree()
root2 = T2.addNodes(None,2)
root2 = T2.addNodes(root2,1)
root2 = T2.addNodes(root2,3)
print("Level order Tree 2 : ",T1.levelOrder(root2))

T = Tree()

print("\nT1 and T2 are same tree or not : ",T.sameTree(root1,root2))