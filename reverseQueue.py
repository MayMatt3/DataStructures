from collections import deque


def input_array():
    arr = input("Enter the elements of the array: ").split()
    return arr


def reverse_array(arr):
    q = deque()

    for item in arr:
        q.append(item)

    reversed_arr = []
    while q:
        reversed_arr.append(q.pop())
    return reversed_arr


if __name__ == "__main__":
    arr = input_array()
    print("Initial Array", arr)

    reverse = reverse_array(arr)
    print("Reversed array:", reverse)
