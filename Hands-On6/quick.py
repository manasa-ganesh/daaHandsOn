import random
import time
import matplotlib.pyplot as plt

def quicksort(array):
    if len(array) <= 1:
        return array
    p = array[len(array) // 2]
    l = [x for x in array if x < p]
    m = [x for x in array if x == p]
    r = [x for x in array if x > p]
    return quicksort(l) + m + quicksort(r)

def benchmark(inputs):
    et = []
    for i in inputs:
        start_time = time.time()
        quicksort(i)
        end_time = time.time()
        et.append(end_time - start_time)
    return et


max_input_size = 200
array_size = list(range(1, max_input_size + 1))

best_case = [list(range(1, n + 1)) for n in array_size]
worst_case = [list(range(n, 0, -1)) for n in array_size]
average_case = [random.sample(range(1, n + 1), n) for n in array_size]

plt.plot(array_size,  benchmark(best_case), label='Best Case')
plt.plot(array_size,  benchmark(worst_case), label='Worst Case')
plt.plot(array_size, benchmark(average_case), label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Benchmark of Non-Random Pivot points')
plt.legend()
plt.show()
