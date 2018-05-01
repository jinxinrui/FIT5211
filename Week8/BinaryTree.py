# !/usr/local/bin/python3

from collections import deque


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return str(self.key)

    def setLeftChild(self, tree):
        assert self.hasLeftChild() is False
        self.leftChild = tree

    def setRightChild(self, tree):
        assert self.hasRightChild() is False
        self.rightChild = tree

    def getLeftChild(self):
        assert self.hasLeftChild()
        return self.leftChild

    def getRightChild(self):
        assert self.hasRightChild()
        return self.rightChild

    def hasLeftChild(self):
        return True if self.leftChild is not None else False

    def hasRightChild(self):
        return True if self.rightChild is not None else False

    def getRoot(self):
        return self

    def preorderPrint(self):
        print(self.key)
        if self.hasLeftChild():
            self.leftChild.preorderPrint()
        if self.hasRightChild():
            self.rightChild.preorderPrint()

    def inorderPrint(self):
        if self.hasLeftChild():
            self.leftChild.inorderPrint()
        print(self.key)
        if self.hasRightChild():
            self.rightChild.inorderPrint()

    def postorderPrint(self):
        if self.hasLeftChild():
            self.leftChild.postorderPrint()
        if self.hasRightChild():
            self.rightChild.postorderPrint()
        print(self.key)

    def measureHeight(self):
        leftHeight = 0
        rightHeight = 0
        if self.hasLeftChild():
            leftHeight = self.leftChild.measureHeight() + 1
        if self.hasRightChild():
            rightHeight = self.rightChild.measureHeight() + 1
        if leftHeight >= rightHeight:
            return leftHeight
        else:
            return rightHeight

    def findValueAtMinimumDepth(self, v):
        que = deque()
        n = 0
        # depth = 0
        que.append([self, 0])
        while len(que) > 0 and n < 50:
            cur = que.pop()

            if str(cur[0]) == str(v):
                return cur[1]
            if cur[0].hasLeftChild():
                que.insert(0, [cur[0].getLeftChild(), cur[1] + 1])
            if cur[0].hasRightChild():
                que.insert(0, [cur[0].getRightChild(), cur[1] + 1])
            n = n + 1
        print("no element")
        return None
    # def depth(self, v)


firstTree = BinaryTree(7)
n0 = BinaryTree(12)
n0.setLeftChild(BinaryTree(5))
n0.setRightChild(BinaryTree(10))
n1 = BinaryTree(8)
n1.setLeftChild(n0)
n1.setRightChild(BinaryTree(9))

n2 = BinaryTree(7)
n2.setLeftChild(BinaryTree(5))
n2.setRightChild(BinaryTree(6))

firstTree.setLeftChild(n1)
firstTree.setRightChild(n2)
firstTree.findValueAtMinimumDepth(20)

print(firstTree)
# def bfs(root):
#     que = deque()
#     que.append(root)
#     while len(que) > 0:
#         cur = que.pop()
#         print(cur.depth)
#         if cur.hasLeftChild():
#             que.append(cur.leftChild)
#         if cur.hasRightChild():
#             que.append(cur.rightChild)
