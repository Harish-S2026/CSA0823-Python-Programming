import random
import time

def weekly_totals(readings):
    return [sum(readings[i:i + 7]) for i in range(0, len(readings), 7)]

def moving_average_naive(readings, window=7):
    if window <= 0 or len(readings) < window:
        return []
    return [sum(readings[i:i + window]) / window for i in range(len(readings) - window + 1)]

def moving_average_running(readings, window=7):
    if window <= 0 or len(readings) < window:
        return []
    total = sum(readings[:window])
    averages = [total / window]
    for i in range(window, len(readings)):
        total += readings[i] - readings[i - window]
        averages.append(total / window)
    return averages

def analyse(readings):
    totals = weekly_totals(readings)
    wettest = max(enumerate(totals, 1), key=lambda item: item[1]) if totals else None
    driest = min(enumerate(totals, 1), key=lambda item: item[1]) if totals else None
    averages = moving_average_running(readings)
    dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]
    return totals, wettest, driest, averages, dry_days

def benchmark(size):
    data = [random.uniform(0, 80) for _ in range(size)]
    start = time.perf_counter()
    moving_average_naive(data)
    naive_time = time.perf_counter() - start
    start = time.perf_counter()
    moving_average_running(data)
    running_time = time.perf_counter() - start
    return naive_time, running_time

if __name__ == "__main__":
    random.seed(8)
    rainfall = [round(random.uniform(0, 60), 1) for _ in range(365)]
    rainfall[4] = 0
    totals, wettest, driest, averages, dry_days = analyse(rainfall)
    print("Weekly totals:", totals)
    print("Wettest week:", wettest)
    print("Driest week:", driest)
    print("First five moving averages:", averages[:5])
    print("Dry days:", dry_days)
    print("Empty input:", moving_average_running([]))
    print("Short input:", moving_average_running([1, 2, 3]))
    for size in (365, 36500, 365000):
        print("Benchmark", size, benchmark(size))
