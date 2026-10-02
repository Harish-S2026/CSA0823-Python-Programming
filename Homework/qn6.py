# Method 1: Using global

count = 0

def increase():
    global count
    count = count + 1

increase()

print("Method 1:", count)


# Method 2: Using return

count = 0

def increase_count(count):
    count = count + 1
    return count

count = increase_count(count)

print("Method 2:", count)