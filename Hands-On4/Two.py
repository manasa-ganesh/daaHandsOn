#Question: Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.

K = int(input("K = "))
N =  int(input("N = "))
given_array=[]
merged_array=[]
def insertion_sort(array):
    for ind in range(1, len(array)):
        ele = array[ind]
        index = ind - 1
        while index >= 0:
            if array[index] > ele:
                array[index + 1] = array[index]
                index -= 1
            else:
                break
        array[index + 1] = ele
    return array

for i in range(K):
    inp=list(map(int,input("Enter sorted array: ").split(" ")))
    given_array.append(inp)
for g_array in given_array:
    merged_array.extend(g_array)
print("Merged array in a sorted order : ",insertion_sort(merged_array))


''' Example/Result: 
K = 3, N =  4
Enter sorted array : 1 3 5 7
Enter sorted array : 2 4 6 8
Enter sorted array : 0 9 10 11
Merged array in a sorted order : [0,1,2,3,4,5,6,7,8,9,10,11]
'''
