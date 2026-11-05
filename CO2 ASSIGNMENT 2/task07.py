# Q7 - Diagnose and redesign: naive recursion -> iterative dynamic programming
import time

def original_naive(n, counter):
    counter[0] += 1
    if n <= 1:
        return 1
    return original_naive(n - 1, counter) + original_naive(n - 2, counter)

def redesigned_loop(n):
    # Keep only the previous two subproblem results.
    if n <= 1:
        return 1
    one_step_back = 1
    two_steps_back = 1
    for _ in range(2, n + 1):
        current = one_step_back + two_steps_back
        two_steps_back = one_step_back
        one_step_back = current
    return one_step_back

if __name__ == "__main__":
    for n in (10, 20, 25, 30):
        calls = [0]
        start = time.perf_counter()
        original = original_naive(n, calls)
        original_time = time.perf_counter() - start
        start = time.perf_counter()
        redesigned = redesigned_loop(n)
        redesigned_time = time.perf_counter() - start
        print(f"n={n}: equal={original == redesigned}, "
              f"naive_calls={calls[0]}, "
              f"naive_time={original_time:.6f}s, "
              f"loop_time={redesigned_time:.6f}s")
    start = time.perf_counter()
    value = redesigned_loop(1000)
    print("n=1000 loop result digits:", len(str(value)),
          "time:", time.perf_counter() - start)
