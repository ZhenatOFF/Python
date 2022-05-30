class TreeNode:
   def __init__(self,data):
      self.left = None
      self.right = None
      self.data = data

   def Insert(self, value):
      newNode=TreeNode(value)
      if self is None:
         self = newNode
      else:
         if value>=self.data:
            if self.right is None:
               self.right = newNode
            else:
               self.right.Insert(value)
         elif value<self.data:
            if self.left is None:
               self.left = newNode
            else:
               self.left.Insert(value)

   def PrintTreeDFS(self):
      if self.left:
         self.left.PrintTreeDFS()
      print( self.data),
      if self.right:
         self.right.PrintTreeDFS()

   def PrintTreeBFS(self):
      h = self.Height()
      for i in range(h):
         self.PrintLevel(i)

   def Height(self):
      if self is None:
         return 0

      rightHeight=0
      leftHeight=0

      if self.right:
         rightHeight = self.right.Height()
      if self.left:
         leftHeight = self.left.Height()

      return max(leftHeight,rightHeight)+1

   def PrintLevel(self, level):
      if self is None:
         return
      if level == 0:
         print(self.data)
      elif level > 0:
         if self.left:
            self.left.PrintLevel(level - 1)
         if self.right:
            self.right.PrintLevel(level - 1)

   def FindMinElem(self):
      if self.left is None:
         return self.data
      else:
         return self.left.FindMinElem()

   def FindMaxElem(self):
      if self.right is None:
         return self.data
      else:
         return self.right.FindMaxElem()

   def VisualizeTree(self):
      height = self.Height()
      for level in range(height):
         for i in range(pow(2,(height-1)-level)*3-3):
            print(" ",end="")
         self.PrintVisualizedLevel(level)
         print("")

   def PrintVisualizedLevel(self, level):
      spaceBetweenNodes = pow(2, self.Height() - level)*3 - 1
      if self is None:
         return
      if level == 0:
         print(self.data," "*spaceBetweenNodes, end="")
      elif level > 0:
         if self.left:
            self.left.PrintVisualizedLevel(level - 1)
         if self.right:
            self.right.PrintVisualizedLevel(level - 1)


tree = TreeNode(5)
tree.Insert(5)
tree.Insert(4)
tree.Insert(-1)
tree.Insert(-2)
tree.Insert(7)
print("\nОбход в глубину:")
tree.PrintTreeDFS()
print(" ")
print("\nОбход в ширину:")
tree.PrintTreeBFS()
print("\nМинимальный элемент:")
print(tree.FindMinElem())
print("\nМаксимальный элемент:")
print(tree.FindMaxElem())
print("\nВизуализация дерева:")
tree.VisualizeTree()