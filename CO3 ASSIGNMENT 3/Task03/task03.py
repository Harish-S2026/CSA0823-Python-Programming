import random
import re
import string
import time
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in re.findall(r"\b[a-z]+\b", text.lower()):
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

def list_count_method(texts, stop):
    words = [word for text in texts for word in re.findall(r"\b[a-z]+\b", text.lower()) if word not in stop]
    return {word: words.count(word) for word in set(words)}

def benchmark(count):
    vocabulary = ["seed", "water", "crop", "price", "loan", "soil", "pest", "yield"]
    texts = [" ".join(random.choices(vocabulary, k=12)) for _ in range(count)]
    start = time.perf_counter()
    frequencies(texts, set())
    dictionary_time = time.perf_counter() - start
    start = time.perf_counter()
    Counter(word for text in texts for word in re.findall(r"\b[a-z]+\b", text.lower()))
    counter_time = time.perf_counter() - start
    start = time.perf_counter()
    list_count_method(texts, set())
    list_time = time.perf_counter() - start
    return dictionary_time, counter_time, list_time

if __name__ == "__main__":
    print(top(frequencies(calls, STOP), 3))
    print("Empty text:", frequencies([""], STOP))
    print("Case and punctuation:", frequencies(["SEEDS, seeds! Price."], STOP))
    random.seed(8)
    for size in (1000, 10000, 100000):
        print("Benchmark", size, benchmark(size))
