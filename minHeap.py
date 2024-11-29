def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[smallest]:
        smallest = l
    if r < n and arr[r] > arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    arr.reverse()


def print_sort(arr):
    for i in arr:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    arr = list(map(int, input("Enter tree values: ").split()))
    heap_sort(arr)
    print("Sorted in descending order: ", end="")
    print_sort(arr)
