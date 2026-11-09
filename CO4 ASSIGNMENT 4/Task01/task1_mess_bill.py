"""
TASK 1.2 - Repaired mess bill processor
Input format: register_number,name,amount
Run: python task1_mess_bill.py [optional_input_file]
"""
from pathlib import Path
import sys

def process_mess_bills(file_name):
    total = 0.0
    report_lines = []
    rejected_lines = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = [part.strip() for part in line.split(",")]
                try:
                    if len(parts) != 3:
                        raise ValueError("expected 3 fields")
                    register_number, name, amount_text = parts
                    amount = float(amount_text)
                    if not register_number or not name or amount < 0:
                        raise ValueError("missing field or negative amount")
                    total += amount
                    report_lines.append(f"{name} {amount:.2f}")
                except ValueError as error:
                    rejected_lines.append((line_number, line, str(error)))
    except FileNotFoundError:
        print(f"Error: file not found: {file_name}")
        return
    except PermissionError:
        print(f"Error: permission denied: {file_name}")
        return
    except UnicodeDecodeError:
        print(f"Error: file is not valid UTF-8: {file_name}")
        return

    print("MESS BILL REPORT")
    print("\\n".join(report_lines))
    print(f"Total: {total:.2f}")
    print("Rejected lines:", rejected_lines)

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "mess_oct.txt"
    process_mess_bills(input_file)
