# !/usr/local/bin/python3


def search(root):
    que = deque()
    que.append(root)
    while len(que) > 0:
        cur = que.pop()
        print(cur.depth)
        if cur.hasLeftChild():
            que.append(cur.leftChild)
        if cur.hasRightChild():
            que.append(cur.rightChild)


def dfs(node):
    print(node.depth)
    if node.hasLeftChild():
        dfs(node.getLeftChild)
    if node.hasRightChild():
        dfs(node.getRightChild)
