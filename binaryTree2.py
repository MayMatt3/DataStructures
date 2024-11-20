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


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def sum_divisible(root):
    if root is None:
        return 0
    totalSum = 0
    totalSum += sum_divisible(root.left)
    if root.val % 5 == 0:
        totalSum += root.val
    totalSum += sum_divisible(root.right)
    return totalSum


if __name__ == "__main__":
    r = None
    values = input("Enter values: ").split()
    for val in values:
        r = insert(r, int(val))
    print("Inorder traversal: ", end="")
    inorder(r)
    print("\nSum of nodes divisible by 5: ", end="")
    print(sum_divisible(r))
