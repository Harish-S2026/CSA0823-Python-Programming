def analyze(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


numbers = [10, 20, 30, 40, 50]

# Method 1
minimum, maximum, average = analyze(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)


# Method 2
result = analyze(numbers)

print("Result =", result)
print("Data type =", type(result))