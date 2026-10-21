
# Task 11: Recommended final design

from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")


def payout(litres, fat, snf):
    """Return the payment rounded to two decimal places."""
    if litres <= 0 or not 2.0 <= fat <= 7.0 or snf <= 0:
        raise ValueError("Invalid milk entry")

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + Decimal(fat_steps) * FAT_STEP_VALUE \
           + Decimal(snf_steps) * SNF_STEP_VALUE

    rate = rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    amount = Decimal(str(litres)) * rate

    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7)]
total = Decimal("0.00")

for litres, fat, snf in entries:
    amount = payout(litres, fat, snf)
    print("Payment:", amount)
    total += amount

print("Total payment:", total)
