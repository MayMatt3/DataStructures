def reverse_order(arr):

    stack = []

    for i in range(len(arr)):
        stack.append(arr[i])

    while len(stack) > 0:
        print(stack[-1], end=" ")
        stack.pop()


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    reverse_order(arr)
