class Linked_List:

  def __init__(self,val):
    self.value = val
    self.next = None

  def insert_first(self,head,val):
    new_node = Linked_List(val)
    new_node.next = head
    return new_node

  def insert_last(self,head,val):
    new_node = Linked_List(val)
    temp = head
    while temp.next!=None:
      temp = temp.next
    temp.next = new_node
    return head

  def insert_mid(self,head,val,pos):
    new_node = Linked_List(val)
    temp = head
    position = 0
    while (position!=pos):
      temp = temp.next
      position += 1
    next_node = temp.next
    temp.next = new_node
    new_node.next = next_node
    return head

  def del_first(self,head):
    temp = head
    head = head.next
    temp.next = None
    return head

  def del_last(self,head):
    temp = head
    while temp.next.next!=None:
      temp = temp.next
    temp.next = None
    return head

  def del_mid(self,head,pos):
    temp = head
    position = 0
    while (position!=pos):
      temp = temp.next
      position += 1
    del_node = temp.next
    temp.next = temp.next.next
    del_node.next = None
    return head
    
  def traverse(self,head):
    temp = head
    while (temp):
      print(temp.value, end = ' ')
      temp = temp.next
      
     
# Driver Code
List = Linked_List(1)
head = List
head = List.insert_first(head,0)
head = List.insert_last(head,3)
head = List.insert_mid(head,2,1)
head = List.insert_mid(head,4,2)
List.traverse(head)

head = List.del_first(head)
List.traverse(head)

head = List.del_last(head)
List.traverse(head)

head = List.del_mid(head,0)
List.traverse(head)
