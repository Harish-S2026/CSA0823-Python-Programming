"""
TASK 3 - Custom exception and robust attendance parser
Includes the completed TODO 1 and TODO 2 program from the assignment.
Run: python task3_exceptions.py
"""
import os
import tempfile

class InvalidRecord(Exception):
    """Raised when a line is not in the expected attendance format."""

def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    register, date, status = (part.strip() for part in parts)
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")
    if not register or not date:
        raise InvalidRecord("register number and date must not be empty")
    return register, date, status

def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    _, _, status = parse_line(line)
                except InvalidRecord as error:
                    errors.append((line_number, str(error)))
                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
    except FileNotFoundError:
        raise
    except PermissionError:
        raise
    except UnicodeDecodeError as error:
        raise ValueError("attendance file has an invalid encoding") from error
    return present, absent, errors

if __name__ == "__main__":
    data = (
        "192311001,2026-10-08,P\\n"
        "192311002,2026-10-08,A\\n"
        "192311003,2026-10-08\\n"
        "192311004,2026-10-08,L\\n"
    )
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(data)
        temp_name = tmp.name

    try:
        print(summarise(temp_name))
    finally:
        os.remove(temp_name)

    # Missing-file demonstration:
    try:
        summarise("file_that_does_not_exist.csv")
    except FileNotFoundError as error:
        print("Handled missing file:", error)
