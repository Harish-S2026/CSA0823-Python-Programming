
# Task 5: Input validation and formatted output

while True:
    try:
        farmer_id = input("Enter farmer ID: ")
        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat percentage: "))
        snf = float(input("Enter SNF percentage: "))

        if litres <= 0:
            print("Litres must be positive.")
            continue

        if not 2.0 <= fat <= 7.0:
            print("Fat must be between 2.0 and 7.0.")
            continue

        if snf <= 0:
            print("SNF must be positive.")
            continue

        break

    except ValueError:
        print("Invalid input. Enter numbers correctly.")

rate = 30 + round((fat - 3.5) / 0.1) * 0.40 \
          + round((snf - 8.5) / 0.1) * 0.30

amount = round(litres * rate, 2)

print(f"{'Farmer ID':15}{'Litres':>10}{'Rate':>10}{'Amount':>12}")
print(f"{farmer_id:15}{litres:10.2f}{rate:10.2f}{amount:12.2f}")
