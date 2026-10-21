
# Task 12: Revised seasonal milk payment calculator

from decimal import Decimal, ROUND_HALF_UP

STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_LIMIT = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")


def money(value):
    """Round money to two decimal places."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def get_rate_card(month):
    """Return the rate card for the selected month."""
    if 4 <= month <= 6:
        return {
            "base": Decimal("32.00"),
            "fat_step": Decimal("0.45")
        }

    return {
        "base": Decimal("30.00"),
        "fat_step": Decimal("0.40")
    }


def rate_per_litre(fat, snf, month):
    """Calculate the rate using the selected season."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    fat_steps = round((fat - STANDARD_FAT) / Decimal("0.1"))
    snf_steps = round((snf - STANDARD_SNF) / Decimal("0.1"))

    card = get_rate_card(month)

    rate = card["base"] + Decimal(fat_steps) * card["fat_step"] \
           + Decimal(snf_steps) * SNF_STEP_VALUE

    return money(rate)


def ten_day_payment(entries, month):
    """Calculate payments and any ten-day volume bonus."""
    total_litres = sum(Decimal(str(item[0])) for item in entries)
    total = Decimal("0.00")

    for litres, fat, snf in entries:
        litres = Decimal(str(litres))

        if litres <= 0 or not Decimal("2.00") <= Decimal(str(fat)) <= Decimal("7.00") or Decimal(str(snf)) <= 0:
            raise ValueError("Invalid milk entry")

        rate = rate_per_litre(fat, snf, month)
        amount = money(litres * rate)
        total += amount

        print("Rate:", rate, "Payment:", amount)

    if total_litres > BONUS_LIMIT:
        bonus = money(total_litres * BONUS_PER_LITRE)
    else:
        bonus = Decimal("0.00")

    return money(total), bonus, money(total + bonus)


entries = [
    (300, 4.25, 8.65),
    (250, 3.50, 8.50)
]

for month in (3, 4):
    print("\nMonth:", month)
    milk_total, bonus, final_total = ten_day_payment(entries, month)
    print("Milk payment:", milk_total)
    print("Bonus:", bonus)
    print("Final payment:", final_total)
