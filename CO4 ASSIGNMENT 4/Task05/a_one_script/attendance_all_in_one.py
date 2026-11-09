"""Task 5(a): one-script attendance utility."""
def read_records(path):
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[2] in ("P", "A"):
                records.append((parts[0], parts[1], parts[2]))
    return records

def percentage(records):
    totals = {}
    for register, date, status in records:
        totals.setdefault(register, {"P": 0, "A": 0})
        totals[register][status] += 1
    return {reg: v["P"] / (v["P"] + v["A"]) * 100
            for reg, v in totals.items() if v["P"] + v["A"]}

def absent_three_days(records):
    by_student = {}
    for reg, date, status in records:
        by_student.setdefault(reg, {})[date] = status
    result = []
    for reg, days in by_student.items():
        dates = sorted(days)
        for i in range(len(dates) - 2):
            if all(days.get(dates[j]) == "A" for j in range(i, i + 3)):
                result.append(reg)
                break
    return result

def write_report(values, path="attendance_report.txt"):
    with open(path, "w", encoding="utf-8") as file:
        for reg, value in sorted(values.items()):
            file.write(f"{reg}: {value:.2f}%\\n")

if __name__ == "__main__":
    sample = [("S01", "2026-10-01", "P"), ("S01", "2026-10-02", "A"),
              ("S01", "2026-10-03", "A"), ("S01", "2026-10-04", "A")]
    values = percentage(sample)
    write_report(values)
    print(values)
    print("Absent for three consecutive recorded days:", absent_three_days(sample))
