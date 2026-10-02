def greet(name, greeting="Hello"):
    print(greeting, name)


# 1. Positional
greet("Harish", "Hi")

# 2. Keyword
greet(name="Harish", greeting="Good Morning")

# 3. Using the default
greet("Harish")

# 4. Swapping argument order with keywords
greet(greeting="Welcome", name="Harish")


# Error example
greet("Harish", greeting="Hi", name="Siva")