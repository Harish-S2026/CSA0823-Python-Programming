def percentage(records):
    totals = {}
    for reg, date, status in records:
        totals.setdefault(reg, {"P": 0, "A": 0})
        totals[reg][status] += 1
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
