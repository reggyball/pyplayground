def heapify(arr, n, i):
    largest = i  # Assume root is largest
    l = 2 * i + 1  # Left child index
    r = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Check if right child exists and is greater than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def build_heap(arr):
    n = len(arr)
    # Start heapifying from the last non-leaf node up to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Example array
arr = [10, 5, 3, 2, 4, 15]  # Inserted 15 at the last position

print("Before build_heap:", arr)
build_heap(arr)
print("After build_heap:", arr)

