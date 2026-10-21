farmer_id = "F101"  # Text
litres = 10         # Quantity in litres
fat = 3.5           # Fat percentage
snf = 8.5           # SNF percentage
shift = "Morning"   # Text

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

rate = BASE_RATE + fat_steps * FAT_STEP_VALUE \
       + snf_steps * SNF_STEP_VALUE

amount = round(litres * rate, 2)

print("Farmer ID:", farmer_id)
print("Rate per litre:", rate)
print("Payment:", amount)
