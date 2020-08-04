class Stack:
  Top = -1

  def __init__(self,size):
    self.stack = [0 for i in range(size)]

  def push(self, value):
    if (Stack.Top!=len(self.stack)-1):
      Stack.Top += 1
      self.stack[Stack.Top] = value
    else:
      print("Overflow: Stack is Full")
  
  def pop(self):
    if (Stack.Top == -1):
      print("Underflow: Stack is Empty")
    else:
      Stack.Top -= 1

  def peek(self):
    if (Stack.Top == -1):
      print("Underflow: Stack is Empty")
    else:
      return (self.stack[Stack.Top])

  def traverse(self):
    if (Stack.Top == -1):
      print("Underflow: Stack is Empty")
    else:
      for i in range(Stack.Top,-1,-1):
        print(self.stack[i], end = " ")

  def is_Full(self):
    if (Stack.Top == len(self.stack)-1):
      return True
    else:
      return False
  
  def is_Empty(self):
    if (Stack.Top == -1):
      return True
    else:
      return False
      
# Driver Code
data = Stack(5)
data.traverse()
data.push(5)
data.push(36)
data.push(43)
data.traverse()
data.push(33)
data.traverse()
print(data.peek())
data.pop()
data.traverse()
print(data.is_Empty())
print(data.is_Full())
