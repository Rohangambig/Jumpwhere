def reverseQueue(queue,k):
    front = 0 
    rear = k - 1

    while front < rear :
        queue[front] = queue[front] ^ queue[rear]
        queue[rear] = queue[front] ^ queue[rear]
        queue[front] = queue[front] ^ queue[rear]
        front += 1
        rear -= 1
    
    return queue 

print(reverseQueue([1,2,3,4,5,6,7,8,9],5))