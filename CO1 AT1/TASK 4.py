
# Task 4: Expressions and operators

import math

fat = 4.2
snf = 8.7
litres = 8.5

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = BASE_RATE + fat_steps * FAT_STEP_VALUE \
       + snf_steps * SNF_STEP_VALUE

amount = round(litres * rate, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate:", round(rate, 2))
print("Amount:", amount)

# Unexpected results
print((4.2 - 3.5) / 0.1)
print(0.1 + 0.2 == 0.3)
print(-7 // 2)

# Difference between rounding methods
x = -2.7
print(round(x))
print(int(x))
print(math.floor(x))

# Validation using comparison chaining
print(2.0 <= fat <= 7.0)
