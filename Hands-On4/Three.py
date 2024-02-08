#Question: Given a sorted array array of size N, the task is to remove the duplicate elements from the array.

def rmv_dupli(arr):
    if not arr:
        return []
    #Empty don't have duplicates
    n = len(arr)
    unq_ptr = 0
    for i in range(1, n):
        if arr[i] != arr[unq_ptr]:
            unq_ptr += 1
            arr[unq_ptr] = arr[i]
    return arr[:unq_ptr + 1]

arr = input("Enter a sorted array : ")
input_array = list(map(int, arr.split()))
output_array = rmv_dupli(input_array)

print(f"Original array: {input_array}")
print(f"Array after removing the duplicate elements: {output_array}")
