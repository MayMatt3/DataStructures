class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


def sum_divisible(root):
    if root is None:
        return 0
    total = 0
    if root.val % 5 == 0:
        total += root.val
    total += sum_divisible(root.left)
    total += sum_divisible(root.right)
    return total


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


if __name__ == "__main__":
    values = list(map(int, input("Enter the tree values: ").split()))
    root = None
    for key in values:
        root = insert(root, key)

    print("Inorder Traversal: ")
    inorder(root)
    print()

    totalSum = sum_divisible(root)
    print(f"\nThe sum of nodes divisible by 5 is: {totalSum}")
