class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if root.data == value:
        return root
    if root.data < value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def calculateSum(root, k, ans):
    if root.right is not None:
        calculateSum(root.right, k, ans)
    if k[0] > 0:
        ans[0] += root.data
        k[0] -= 1
    else:
        return
    if root.left is not None:
        calculateSum(root.left, k, ans)


def sum_k_largest(root, k):
    ans = [0]
    calculateSum(root, [k], ans)
    return ans[0]



if __name__ == "__main__":
    root = None
    values = input("Enter values: ").split()
    for value in values:
        root = insert(root, int(value))
    print("Inorder traversal: ", end="")
    inorder(root)
    print()
    k = int(input("Enter value of k: "))
    print(sum_k_largest(root, k))