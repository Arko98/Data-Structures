class Linear_Hash_Table:

  def __init__(self, size):
    self.table = [0 for i in range(size)]
    self.size = size

  def hash_function(self, key):
    index = key % self.size
    return index

  def insert(self, key):
    index = self.hash_function(key)
    temp = index
    if (self.table[index] == 0):
      self.table[index] = key
      print("Insertion Successful")
    else:
      while(self.table[temp]!=0):
        temp += 1
        if (temp==self.size):
          print("Hash Table is Full, insertion unsucessfull")
          break
      if (temp!=self.size):
        self.table[temp] = key
        print("Insertion Successful")
      
  def search(self, key):
    index = self.hash_function(key)
    temp = index
    if (self.table[index] == key):
      print("Search Successfull")
      return index
    else:
      while(self.table[temp]!=key):
        temp += 1
        if (temp==self.size):
          print("Search unsucessfull")
          break
      if (temp!=self.size and self.table[temp]==key):
        print("Search Successfull")
        return temp

  def delete(self, key):
    index = self.hash_function(key)
    temp = index
    if (self.table[index] == key):
      self.table[index] = 0
      print("Deletion Successful")
    else:
      while(self.table[temp]!=key):
        temp += 1
        if (temp==self.size):
          print("Deletion unsucessfull, key not found in Hash Table")
          break
      if (temp!=self.size and self.table[temp]==key):
        self.table[temp] = 0
        print("Deletion Successful")

  def traverse(self):
    print(self.table)

  def is_Full(self):
    index = 0
    while (index<self.size and self.table[index]!=0):
      index += 1
    if (index==self.size):
      return True
    else:
      return False
      
      
# Driver Code
Table = Linear_Hash_Table(10)
Table.insert(5)
Table.traverse()
Table.insert(2)
Table.traverse()
Table.insert(35)
Table.traverse()
Table.insert(22)
Table.traverse()
Table.insert(222)
Table.traverse()
Table.insert(2222)
Table.traverse()
Table.delete(222)
Table.traverse()
Table.delete(22)
Table.traverse()
Table.is_Full()
Table.search(222)
Table.search(5)
