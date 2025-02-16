class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = self.right = None 

class TreeNode:
    def addElement(self,arr):
        def Helper(l,r):
            if l > r: return 

            m = (l + r) // 2
            root = Node(arr[m])
            root.left = Helper(l,m-1)
            root.right = Helper(m+1,r)
            return root

        return Helper(0,len(arr)-1)

    def Display(self,root):
        if root: 
            self.Display(root.left)
            print(root.data,end=" ")
            self.Display(root.right)

T = TreeNode()
arr = [-10,-3,0,5,9]

root = T.addElement(arr)
T.Display(root)