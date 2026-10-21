
# Task 6: Functions for milk payment

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate the rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE \
           + snf_steps * SNF_STEP_VALUE

    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the payment for one entry."""
    return round(litres * rate_per_litre(fat, snf), 2)


def ten_day_total(payments):
    """Calculate the total payment for ten days."""
    total = 0.0

    for litres, fat, snf in payments:
        total += payout(litres, fat, snf)

    return round(total, 2)


entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

for entry in entries:
    print("Payment:", payout(*entry))

print("Ten-day total:", ten_day_total(entries))
