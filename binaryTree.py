from collections import deque


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)
    return root


def preorder_dfs(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder_dfs(root.left)
    preorder_dfs(root.right)


def postorder_dfs(node):
    if node is None:
        return
    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.data, end=' ')


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    key = 6
    root = insert(root, key)
    print("Postorder Traversal: ", end="")
    postorder_dfs(root)
    print()
