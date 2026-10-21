
# Task 10: Float versus Decimal benchmark

from decimal import Decimal
from time import perf_counter

def float_total(payments):
    """Calculate the total using float."""
    total = 0.0
    for amount in payments:
        total += float(amount)
    return total


def decimal_total(payments):
    """Calculate the total using Decimal."""
    total = Decimal("0.00")
    for amount in payments:
        total += Decimal(amount)
    return total


for n in (300, 6000, 150000):
    payments = ["33.40"] * n

    start = perf_counter()
    f_total = float_total(payments)
    float_time = perf_counter() - start

    start = perf_counter()
    d_total = decimal_total(payments)
    decimal_time = perf_counter() - start

    print("\nPayments:", n)
    print("Float total:", f_total)
    print("Decimal total:", d_total)
    print("Difference:", abs(Decimal(str(f_total)) - d_total))
    print("Float time:", float_time)
    print("Decimal time:", decimal_time)
