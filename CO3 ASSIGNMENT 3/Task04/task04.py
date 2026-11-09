import random
import time

ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (ai_elective | iot_elective)

def benchmark(size):
    values = list(range(size))
    value_set = set(values)
    target = size - 1
    start = time.perf_counter()
    target in values
    list_time = time.perf_counter() - start
    start = time.perf_counter()
    target in value_set
    set_time = time.perf_counter() - start
    other = set(random.sample(range(size * 2), size))
    start = time.perf_counter()
    set(values) & other
    set_time_intersection = time.perf_counter() - start
    start = time.perf_counter()
    [x for x in values if x in other]
    nested_time = time.perf_counter() - start
    return list_time, set_time, nested_time, set_time_intersection

if __name__ == "__main__":
    print("clash      :", sorted(both))
    print("exactly one:", sorted(exactly_one))
    print("neither    :", sorted(neither))
    print("Empty electives:", set() & set(), set() ^ set())
    print("Identical electives:", ai_elective & ai_elective, ai_elective ^ ai_elective)
    print("Duplicate removal:", len(set(["A", "A", "B"])))
    random.seed(8)
    for size in (10000, 100000, 1000000):
        print("Benchmark", size, benchmark(size))
