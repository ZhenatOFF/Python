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
       
   def ReadFromFile(self,fileName):
      file = open(fileName)
      values = file.read().split(" ")
      for i in values:
         self.Insert(int(i))

   def VisualizeBinaryTree(self):
      height = self.Height()
      nodes = self.GetLevelsDict()
      for level in range(height):
         firstOffset = (pow(2, height-(level+1))-1)*3
         print(" "*firstOffset,end="")
         for i in range(pow(2,level)):
            if nodes[level][i]:
               print(nodes[level][i].data," "*(3-len(str(nodes[level][i].data))),end="")
            elif nodes[level][i] is None:
               print("###",end="")

            spaceBetweenNodes = (pow(2,height-level)-1)*3
            print(" "*spaceBetweenNodes,end="")

         print("")

   def GetLevelsDict(self):
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
tree.VisualizeBinaryTree()

'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 460
HEIGHT = 480
FPS = 30
pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Визуализация дерева")
clock = pygame.time.Clock()

running = True
while running:
   clock.tick(FPS)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False


   # Рендеринг
   sc.fill(WHITE)

   pygame.display.flip()

pygame.quit()
'''