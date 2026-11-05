# Q4 - Compare string construction approaches
import time
import statistics

def build_plus(parts):
    text = ""
    for part in parts:
        text += part + ";"
    return text

def build_join(parts):
    return ";".join(parts) + (";" if parts else "")

def build_fstring(parts):
    pieces = []
    for index, part in enumerate(parts):
        pieces.append(f"{part};")
    return "".join(pieces)

def benchmark(n, repeats=3):
    items = [f"Item{i}:Rs{i % 50}" for i in range(n)]
    results = {}
    outputs = {}
    for name, function in [("+=", build_plus), ("join", build_join),
                           ("f-string + join", build_fstring)]:
        times = []
        for _ in range(repeats):
            start = time.perf_counter()
            result = function(items)
            times.append(time.perf_counter() - start)
        outputs[name] = result
        results[name] = (times, statistics.mean(times))
    assert outputs["+="] == outputs["join"] == outputs["f-string + join"]
    return len(outputs["join"]), results

if __name__ == "__main__":
    for size in (1_000, 10_000, 200_000):
        length, results = benchmark(size)
        print(f"Lines={size}, output length={length}")
        for name, (times, average) in results.items():
            print(f"  {name:16} runs={times} average={average:.6f}s")
