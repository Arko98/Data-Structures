class Binary_Tree:

  def __init__(self,val):
    self.value = val
    self.left = None
    self.right = None

  def preorder(self,root):
    if root:
      print(root.value,end = ' ')
      self.preorder(root.left)
      self.preorder(root.right)

  def inorder(self,root):
    if root:
      self.inorder(root.left)
      print(root.value, end = ' ')
      self.inorder(root.right)

  def postorder(self, root):
    if root:
      self.postorder(root.left)
      self.postorder(root.right)
      print(root.value, end = ' ')

  def depth(self, root):
    if root == None:
      return 0
    else:
      l_depth = self.depth(root.left) 
      r_depth = self.depth(root.right)
      depth_value = max(l_depth,r_depth)+1
      return depth_value
  
# Driver Code
root = Binary_Tree(1)
root.left = Binary_Tree(2)
root.right = Binary_Tree(3)
root.left.left = Binary_Tree(4)
root.left.right = Binary_Tree(5)
root.right.left = Binary_Tree(6)

print("Preorder Traversal of Tree: ")
print(root.preorder(root))
print("Inorder Traversal of Tree: ")
print(root.inorder(root))
print("Postorder Traversal of Tree: ")
print(root.postorder(root))
print("Postorder Traversal of Tree: {}".format(root.depth(root)))
