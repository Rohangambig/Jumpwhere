q1 = []
q2 = []

def push(x):
    q1.append(x)

def pop():
    global q1 , q2

    while len(q1) > 1:
        q2.append(q1.pop(0))
    
    q1.pop(0)   
    q1 , q2 = q2, []

def Top():
    global q1 
    
    size = len(q1)-1
    return q1[size]

push(1)
push(3)
push(5)
print(q1)
pop()
print(q1)
push(6)
push(8)
print(q1)
pop()
print(q1)
print(Top())