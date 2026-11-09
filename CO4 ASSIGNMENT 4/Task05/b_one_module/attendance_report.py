def write_report(values, path="attendance_report.txt"):
    with open(path, "w", encoding="utf-8") as file:
        for reg, value in sorted(values.items()):
            file.write(f"{reg}: {value:.2f}%\\n")
