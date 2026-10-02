def convert(temp, unit):
    if unit == "C":
        result = (temp * 9/5) + 32
        return result, "F"
    elif unit == "F":
        result = (temp - 32) * 5/9
        return result, "C"
    else:
        return "Invalid unit", ""

temp = 25
unit = "C"

result, new_unit = convert(temp, unit)

print("Temperature =", result, new_unit)