class Queue:
  Front = -1
  Rear = -1

  def __init__(self,size):
    self.queue = [0 for i in range(size)]

  def enqueue(self,value):
    if (Queue.Front==Queue.Rear==-1):
        Queue.Front += 1
        Queue.Rear += 1
        self.queue[Queue.Rear] = value
    elif (Queue.Front<Queue.Rear or Queue.Front==Queue.Rear==0):
        Queue.Rear += 1
        self.queue[Queue.Rear] = value
    else:
      print("Overflow: Queue is Full")

  def dequeue(self):
    if (Queue.Front<=Queue.Rear or Queue.Front==Queue.Rear!=-1):
      Queue.Front += 1
    else:
      print("Underflow: Queue is Empty")

  def peek_front(self):
    if (Queue.Front==-1 or Queue.Front>Queue.Rear):
      print("Underflow: Queue is Empty")
    else:
      return (self.queue[Queue.Front])

  def peek_rear(self):
    if (Queue.Rear==-1 or Queue.Front>Queue.Rear):
      print("Underflow: Queue is Empty")
    else:
      return (self.queue[Queue.Rear])

  def traverse(self):
    if (Queue.Front==Queue.Rear==-1 or Queue.Front>Queue.Rear):
      print("Underflow: Stack is Empty")
    else:
      for i in range(Queue.Front,Queue.Rear+1,1):
        print(self.queue[i], end = " ")

  def is_Full(self):
    if (Queue.Front==0 and Queue.Rear==len(self.queue)-1):
      return True
    else:
      return False
  
  def is_Empty(self):
    if (Queue.Front==Queue.Rear==-1 or Queue.Front>Queue.Rear):
      return True
    else:
      return False
      
# Driver Code
data = Queue(5)
data.traverse()
print('\n')
data.enqueue(5)
data.enqueue(36)
data.enqueue(43)
data.traverse()
print('\n')
data.enqueue(33)
data.traverse()
print('\n')
print(data.peek_front())
print('\n')
print(data.peek_rear())
print('\n')
data.dequeue()
data.traverse()
print('\n')
data.dequeue()
data.traverse()
print('\n')
print(data.is_Empty())
print(data.is_Full())
