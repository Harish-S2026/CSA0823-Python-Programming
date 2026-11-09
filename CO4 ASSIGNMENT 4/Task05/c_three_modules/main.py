from attendance.reader import read_records
from attendance.stats import percentage, absent_three_days
from attendance.report import write_report

if __name__ == "__main__":
    records = [("S01", "2026-10-01", "P"), ("S01", "2026-10-02", "A"),
               ("S01", "2026-10-03", "A"), ("S01", "2026-10-04", "A")]
    values = percentage(records)
    write_report(values)
    print(values)
    print(absent_three_days(records))
