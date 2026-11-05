# Q6 - Staircase count: naive recursion, memoisation and loop
from functools import lru_cache
import sys
import time

naive_calls = 0
memo_calls = 0

def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_loop(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

if __name__ == "__main__":
    print("Hand-check:", [ways_loop(n) for n in range(1, 7)])
    for n in (10, 20, 25, 30):
        naive_calls = 0
        naive_value = ways_naive(n)
        memo_calls = 0
        ways_memo.cache_clear()
        memo_value = ways_memo(n)
        print(f"n={n}: naive={naive_value}, calls={naive_calls}; "
              f"memo={memo_value}, calls={memo_calls}")
    ways_memo.cache_clear()
    try:
        print("Memoised n=1000:", ways_memo(1000))
    except RecursionError as error:
        print("RecursionError:", error)
        print("Recursion limit:", sys.getrecursionlimit())
    start = time.perf_counter()
    iterative_value = ways_loop(1000)
    print("Loop n=1000 digits:", len(str(iterative_value)),
          "time:", time.perf_counter() - start)
