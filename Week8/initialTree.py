# !/usr/local/bin/python3


from Week8.BinaryTree import BinaryTree


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

firstTree.getRoot()
firstTree.postorderPrint()
firstTree.inorderPrint()

firstTree.measureHeight()
firstTree.findValueAtMinimumDepth(7)
