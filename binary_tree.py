import random
import timeit

class BinaryTree:

    def __init__(self, item=None):
        print("tree made")
        self.key = item
        self.leftChild = None
        self.rightChild = None

    def insert(self, new):
        if self.key is None:
            self.key = BinaryTree(new)
        elif self.key > new:
            self.insert_left(new)
        elif self.key < new:
            self.insert_right(new)

    def insert_left(self, new):
        if self.leftChild is None:
            self.leftChild = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self,new):
        if self.rightChild is None:
            self.rightChild = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.rightChild = self.rightChild
            self.rightChild = t

    def find(self, value):
        print("here")
        if self.key is not None:
            return self._find(value, self)
        else:
            return False

    def _find(self, value, item):
        print("here")
        if value == item.key:
            return True
        elif value < item.key and item.leftChild is not None:
            return self._find(value, item.leftChild)
        elif value > item.key and item.rightChild is not None:
            return self._find(value, item.rightChild)
        print("not found")
        return False

    def printTree(self):
        if self is not None:
            self._printTree(self)

    def _printTree(self, cur_node):
        if cur_node is not None:
            self._printTree(cur_node.leftChild)
            print(str(cur_node.key))
            self._printTree(cur_node.rightChild)
    def printstuff(self):
        print("stufffffff")

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key





