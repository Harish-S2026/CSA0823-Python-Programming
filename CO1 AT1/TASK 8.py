
# Task 8: Ten-day payment total

payments = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

total = 0.0

for litres, fat, snf in payments:
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
    amount = round(litres * rate, 2)

    print("Payment:", amount)
    total += amount

print("Ten-day total:", round(total, 2))
