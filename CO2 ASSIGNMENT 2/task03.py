# Q3 - Vehicle registration number validation (no regular expressions)
def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    if not reg[0:2].isalpha():
        return False
    if not reg[2:4].isdigit():
        return False
    if not reg[4:-4].isalpha():
        return False
    if len(reg[4:-4]) not in (1, 2):
        return False
    if not reg[-4:].isdigit():
        return False
    return True

def format_receipt(reg):
    reg = normalise(reg)
    if not is_valid(reg):
        raise ValueError("Invalid registration number")
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"

if __name__ == "__main__":
    samples = ["tn 09 ab 1234", "KA-01-M-0007", "Tn09Ab1234",
               "TN9AB1234", "TN 22 1234 AB", "MH 12 XY 9876"]
    for raw in samples:
        reg = normalise(raw)
        print(f"{raw:15} -> {reg:11} "
              f"{'valid' if is_valid(reg) else 'INVALID'}")
    print("Receipt:", format_receipt("tn 09 ab 1234"))
    # For a 9-character value s[-4:] is its last four characters;
    # s[4:-4] is the single character between the first 4 and last 4.
    # For a 10-character value s[4:-4] contains two characters.
