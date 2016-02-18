# from http://stackoverflow.com/a/28864021

class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, v):
        if (self.root == None):
            self.root = Node(v)
        else:
            self._add(v, self.root)

    def _add(self, v, node):
        if (v < node.value):
            if (node.left is not None):
                self._add(v, node.left)
            else:
                node.left = Node(v)
        else:
            if (node.right is not None):
                self._add(v, node.right)
            else:
                node.right = Node(v)

    def find(self, v):
        if (self.root is not None):
            return self._find(v, self.root)
        else:
            return None

    def _find(self, v, node):
        if (v == node.value):
            return node
        elif (v < node.value and node.left is not None):
            self._find(v, node.left)
        elif (v > node.value and node.right is not None):
            self._find(v, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if (self.root is not None):
            self._printTree(self.root)

    def _printTree(self, node):
        if (node is not None):
            self._printTree(node.left)
            print str(node.value) + ' '
            self._printTree(node.right)
