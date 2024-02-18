class MinHeap:
    def _init_(self):
        self.heaparray = []
    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heaparray) and self.heaparray[left] < self.heaparray[smallest]:
            smallest = left

        if right < len(self.heaparray) and self.heaparray[right] < self.heaparray[smallest]:
            smallest = right

        if smallest != i:
            self.heaparray[i], self.heaparray[smallest] = self.heaparray[smallest], self.heaparray[i]
            self.heapify(smallest)

    def build_min_heap(self, arr):
        self.heaparray = arr[:]
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.heapify(i)

    def pop_root(self):
        if not self.heaparray:
            return None

        root = self.heaparray[0]
        last_element = self.heaparray.pop()
        if self.heaparray:
            self.heaparray[0] = last_element
            self.heapify(0)
        return root

    def insert(self, value):
        self.heaparray.append(value)
        i = len(self.heaparray) - 1
        while i != 0 and self.heaparray[(i - 1) // 2] > self.heaparray[i]:
            self.heaparray[i], self.heaparray[(i - 1) // 2] = (
                self.heaparray[(i - 1) // 2],
                self.heaparray[i],
            )
            i = (i - 1) // 2

min_heap = MinHeap()
print("Enter an array:")
arr=list(map(int,input().split(" ")))
min_heap.build_min_heap(arr)
print("Initial Heap array: ",min_heap.heaparray)
min_heap.insert(2)
print("Heap array: ",min_heap.heaparray)
root = min_heap.pop_root()
print("Removed node from heap:", root)
print("Heap array: ",min_heap.heaparray)
root = min_heap.pop_root()
print("Removed node from heap:", root)
print("Heap array: ",min_heap.heaparray)
