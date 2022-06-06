import pygame

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

   def IterativeInsert(self, value):
      newNode = TreeNode(value)
      x = self
      y = None #нужен для трейлинга

      while x!=None:
         y=x
         if value<x.data:
            x = x.left
         else:
            x = x.right

      if y is None:
         y=newNode
      elif value<y.data:
         y.left = newNode
      else:
         y.right = newNode



   def PrintTreeDFS(self):
      if self.left:                         #сначала пробегаемся по левой ветке
         self.left.PrintTreeDFS()
      print( self.data),                    #потом корень
      if self.right:
         self.right.PrintTreeDFS()          #потом пробегаемся по правой ветке

   def PrintTreeBFS(self):
      h = self.Height()
      for i in range(h):
         self.PrintLevel(i)
         print("")

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
         print(self.data," ", end="")
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

   def ReadFromFile(self,fileName):
      file = open(fileName)
      values = file.read().split(" ")
      for i in values:
         self.IterativeInsert(int(i))

   def VisualizeBinaryTree(self): #метод для отрисовки дерева в консоли
      height = self.Height()
      nodes = self.GetLevelsDict()          #получаем словарь с элементами
      for level in range(height):
         firstOffset = (pow(2, height-(level+1))-1)*3         #рассчитываем первый отступ на уровне
         print(" "*firstOffset,end="")                        #отрисовываем этот отступ
         for i in range(pow(2,level)):                        #пробегаем по каждомц элементу на уровне
            if nodes[level][i]:                               #если элемент есть, то печатаем его
               print(nodes[level][i].data," "*(3-len(str(nodes[level][i].data))),end="")
            elif nodes[level][i] is None:                     #если нет, то вместо него ###
               print("###",end="")

            spaceBetweenNodes = (pow(2,height-level)-1)*3     #рассчитываем отступы между элементами на уровне
            print(" "*spaceBetweenNodes,end="")               #и печатаем этот отступ после каждого элемента

         print("")                                            #делаем переход на следующий уровень

   def GetLevelsDict(self):    #метод для получения словаря с уровнем в качестве ключа и массивом узлов в качестве значения
      nodes = {0:[self]}
      height = self.Height()
      for level in range(1,height):
         nodes[level]=[]
         for i in range(pow(2,level-1)):
            if nodes[level-1][i] is None:
               nodes[level].append(None)
               nodes[level].append(None)
            else:
               if nodes[level-1][i].left:
                  nodes[level].append(nodes[level-1][i].left)
               elif nodes[level-1][i].left is None:
                  nodes[level].append(None)
               if nodes[level - 1][i].right:
                  nodes[level].append(nodes[level - 1][i].right)
               elif nodes[level - 1][i].right is None:
                  nodes[level].append(None)

      return nodes


tree = TreeNode(5)
tree.ReadFromFile("task.txt")
tree.IterativeInsert(30)
print("\nОбход в глубину:")
tree.PrintTreeDFS()
print(" ")
tree.PrintLevel(2)
print("\nОбход в ширину:")
tree.PrintTreeBFS()
print("\nМинимальный элемент:")
print(tree.FindMinElem())
print("\nМаксимальный элемент:")
print(tree.FindMaxElem())
print("\nВизуализация дерева:")
tree.VisualizeBinaryTree()
