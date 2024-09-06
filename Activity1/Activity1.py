def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
arr = [23, 89, 7, 56, 44]
print("Array before Bubble Sort",arr)


arr = bubble_sort(arr)
print("Array after Bubble Sort",arr)
print()
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage
arr = [12, 78, 91, 34, 62]
print("Array before Insertion Sort",arr)


insertion_sort(arr)
print("Array after Insertion Sort",arr)
print()

def selection_sort_desc(arr):

    for i in range(len(arr)):
        max_idx = i
        for j in range(i + 1, len(arr)):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]


# Example usage
arr = [5, 99, 48, 15, 67]
print("Array before Selection Sort",arr)

selection_sort_desc(arr)
print("Array after Selection Sort",arr)
print()

def insertion_sort_desc(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage
arr = [38, 82, 25, 74, 13]
print("Array before Insertion Sort",arr)


insertion_sort_desc(arr)
print("Array after Insertion Sort",arr)
print()

def sort_array(arr):

    arr_asc = sorted(arr)
    arr_desc = sorted(arr, reverse=True)
    return arr_asc, arr_desc

# Example usage
arr = [7, 56, 91, 34, 48, 15, 25, 74]
print("Array before sorting",arr)

arr_asc, arr_desc = sort_array(arr)
print("Array in ascending order",arr_asc)

print("Array in descending order",arr_desc)
print()

def selection_sort(arr):
    arr = [23, 89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("Array before Selection Sort",arr)


for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
selection_sort(arr)
print("Array after Selection Sort",arr)
print()

def even_odd(arr):
    arr = [23, 89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]

even_values = [x for x in arr if x % 2 == 0]
odd_values = [x for x in arr if x % 2 != 0]
even_odd(arr)
print("Even values:",even_values)

print("Odd values:",odd_values)
print()