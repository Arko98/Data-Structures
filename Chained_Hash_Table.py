class Chained_Hash_Table:

  def __init__(self, size):
    self.table = [[0] for i in range(size)]
    self.size = size

  def hash_function(self, key):
    index = key % self.size
    return index

  def insert(self, key):
    index = self.hash_function(key)
    temp = index
    if (self.table[index][0] == 0):
      self.table[index][0] = key
      print("Insertion Successful")
    else:
      self.table[index].append(key)
      print("Insertion Successful")
      
  def search(self, key):
    index = self.hash_function(key)
    i = 0
    while (i<len(self.table[index])):
      if (self.table[index][i]==key):
        print("Search Successfull")
        return (index,i)
      i += 1
    if (i==len(self.table[index])):
      print("Search Unsuccessfull, key not found")

  def delete(self, key):
    index = self.hash_function(key)
    i = 0
    while (i<len(self.table[index])):
      if (self.table[index][i]==key):
        del self.table[index][i]
        print("Deletion Successfull")
        break
      i += 1
    if (i==len(self.table[index])):
      print("Deletion Unsuccessfull, key not found")

  def traverse(self):
    print(self.table)
    
    
# Driver Code
Table = Chained_Hash_Table(10)
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
Table.search(222)
Table.search(5)
