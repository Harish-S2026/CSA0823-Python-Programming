import copy
import sys
import time

rows, cols = 3, 4
bad = [[0] * cols] * rows
bad[0][1] = 7
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

stops = {(13.0827, 80.2707): "Chennai Central", (13.0418, 80.2341): "T. Nagar"}
original = [[1, 2], [3, 4]]
alias = original
shallow_slice = original[:]
shallow_copy = copy.copy(original)
deep = copy.deepcopy(original)
original[0][0] = 99
original[1].append(5)

tuple_with_list = ([1, 2], "zone")
tuple_with_list[0].append(3)

if __name__ == "__main__":
    print("bad :", bad)
    print("good:", good)
    print(bad[0] is bad[1], good[0] is good[1])
    print(stops[(13.0418, 80.2341)])
    print("Aliasing:", alias is original)
    print("Shallow slice:", shallow_slice)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep)
    print("Tuple containing list:", tuple_with_list)
    print("List size:", sys.getsizeof(list(range(1000000))))
    print("Tuple size:", sys.getsizeof(tuple(range(1000000))))
    values = list(range(100000))
    start = time.perf_counter()
    tuple(values)
    tuple_create = time.perf_counter() - start
    start = time.perf_counter()
    list(values)
    list_create = time.perf_counter() - start
    start = time.perf_counter()
    values[50000]
    list_index = time.perf_counter() - start
    tuple_values = tuple(values)
    start = time.perf_counter()
    tuple_values[50000]
    tuple_index = time.perf_counter() - start
    print("Creation times:", tuple_create, list_create)
    print("Index times:", tuple_index, list_index)
