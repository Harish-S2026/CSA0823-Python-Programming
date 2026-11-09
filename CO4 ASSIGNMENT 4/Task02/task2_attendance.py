"""
TASK 2 - Monthly biometric attendance processor
Input files: daily CSV-like text files with register_number,date,status
Run: python task2_attendance.py [folder]
"""
from pathlib import Path
from collections import defaultdict
import sys

def process_month(folder_name):
    folder = Path(folder_name)
    counts = defaultdict(lambda: {"P": 0, "A": 0})
    damaged = []

    try:
        daily_files = sorted(folder.glob("*.txt"))
        for file_path in daily_files:
            try:
                with file_path.open("r", encoding="utf-8") as file:
                    for line_number, line in enumerate(file, start=1):
                        text = line.strip()
                        if not text:
                            continue
                        fields = [x.strip() for x in text.split(",")]
                        if len(fields) != 3:
                            damaged.append((file_path.name, line_number, text, "expected 3 fields"))
                            continue
                        register, date, status = fields
                        if not register or not date or status not in ("P", "A"):
                            damaged.append((file_path.name, line_number, text, "invalid field or status"))
                            continue
                        counts[register][status] += 1
            except (PermissionError, UnicodeDecodeError, OSError) as error:
                damaged.append((file_path.name, 0, "", str(error)))

        attendance_rows = []
        below_75 = []
        for register, value in sorted(counts.items()):
            total = value["P"] + value["A"]
            percentage = (value["P"] / total * 100) if total else 0
            row = f"{register},{value['P']},{value['A']},{percentage:.2f}%"
            attendance_rows.append(row)
            if percentage < 75:
                below_75.append(row)

        with (folder / "attendance_summary.csv").open("w", encoding="utf-8") as out:
            out.write("Register Number,Present,Absent,Percentage\\n")
            out.write("\\n".join(attendance_rows))
        with (folder / "below_75.csv").open("w", encoding="utf-8") as out:
            out.write("Register Number,Present,Absent,Percentage\\n")
            out.write("\\n".join(below_75))
        with (folder / "damaged_lines.log").open("w", encoding="utf-8") as out:
            for item in damaged:
                out.write(",".join(map(str, item)) + "\\n")

        print(f"Processed {len(daily_files)} daily files.")
        print(f"Students processed: {len(counts)}")
        print(f"Damaged records/files: {len(damaged)}")
        print("Reports written to", folder.resolve())
    except FileNotFoundError:
        print(f"Input folder not found: {folder}")

if __name__ == "__main__":
    process_month(sys.argv[1] if len(sys.argv) > 1 else "attendance_input")
