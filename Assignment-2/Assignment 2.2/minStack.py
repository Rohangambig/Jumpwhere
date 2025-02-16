class Stack:
    def __init__(self):
        self.stack = []

    def Push(self,data):
        self.stack.append(data)
    
    def Pop(self):
        self.stack.pop()

    def Top(self):
        return self.stack[-1]

    def minStack(self):
        minimum = float('inf')
        arr = self.stack 

        for num in arr:
            minimum = min(minimum,num)
        
        return minimum

S = Stack()
S.Push(-2)
S.Push(0)
S.Push(-3)

print(S.minStack())

S.Pop()
print(S.Top())
print(S.minStack())