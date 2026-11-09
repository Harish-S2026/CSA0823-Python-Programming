import random
import sys
import time

def clean_loop(readings):
    valid = []
    fahrenheit = []
    for value in readings:
        if -50 <= value <= 50:
            valid.append(value)
            fahrenheit.append(value * 9 / 5 + 32)
    return valid, fahrenheit

def clean_comprehension(readings):
    valid = [value for value in readings if -50 <= value <= 50]
    fahrenheit = [value * 9 / 5 + 32 for value in valid]
    return valid, fahrenheit

def clean_map_filter(readings):
    valid = list(filter(lambda value: -50 <= value <= 50, readings))
    fahrenheit = list(map(lambda value: value * 9 / 5 + 32, valid))
    return valid, fahrenheit

def alarm_minutes(readings):
    return [minute for minute, value in enumerate(readings, 1) if not 2 <= value <= 8]

def benchmark(size):
    data = [random.uniform(-60, 60) for _ in range(size)]
    results = []
    for function in (clean_loop, clean_comprehension, clean_map_filter):
        start = time.perf_counter()
        result = function(data)
        results.append((time.perf_counter() - start, result))
    return [(elapsed, len(result[0])) for elapsed, result in results]

if __name__ == "__main__":
    readings = [4.5, 7.2, 55.0, -60.0, 1.5, 9.0, 3.0]
    print("Loop:", clean_loop(readings))
    print("Comprehension:", clean_comprehension(readings))
    print("Map/filter:", clean_map_filter(readings))
    print("Alarm minutes:", alarm_minutes(readings))
    print("Dictionary comprehension:", {i: value for i, value in enumerate(readings, 1) if -50 <= value <= 50})
    print("Set comprehension:", {value for value in readings if -50 <= value <= 50})
    print("All valid:", clean_comprehension([3, 4, 5]))
    print("All invalid:", clean_comprehension([55, -60]))
    print("List memory:", sys.getsizeof([x for x in range(1000)]))
    print("Generator memory:", sys.getsizeof(x for x in range(1000)))
    random.seed(8)
    for size in (10000, 100000, 1000000):
        print("Benchmark", size, benchmark(size))
