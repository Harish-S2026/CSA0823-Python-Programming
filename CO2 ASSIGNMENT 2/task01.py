# Q1 - Electricity subsidy eligibility
def decision_separate(units, ration_card, senior_over_80):
    results = []
    if units <= 100:
        results.append("Full subsidy")
    if 101 <= units <= 200 and ration_card:
        results.append("Partial subsidy")
    if units > 200 and senior_over_80:
        results.append("Special senior subsidy")
    if not results:
        results.append("No subsidy")
    return results

def decision_elif(units, ration_card, senior_over_80):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    elif units > 200:
        if senior_over_80:
            return "Special senior subsidy"
        else:
            return "No subsidy"

def decision_match(units, ration_card, senior_over_80):
    # Match-case alternative (Python 3.10+); guards express the conditions.
    match units:
        case x if x <= 100:
            return "Full subsidy"
        case x if 101 <= x <= 200 and ration_card:
            return "Partial subsidy"
        case x if 101 <= x <= 200:
            return "No subsidy"
        case x if x > 200 and senior_over_80:
            return "Special senior subsidy"
        case _:
            return "No subsidy"

if __name__ == "__main__":
    households = [
        ("H1", 100, False, False), ("H2", 101, True, False),
        ("H3", 101, False, False), ("H4", 150, True, False),
        ("H5", 200, True, False), ("H6", 200, False, True),
        ("H7", 201, False, True), ("H8", 201, True, False)
    ]
    print("ID  Units  Ration  Age>80  Separate-if  if-elif-else")
    for name, units, card, senior in households:
        print(f"{name:2}  {units:5}  {str(card):6}  {str(senior):6}  "
              f"{decision_separate(units, card, senior)}  "
              f"{decision_elif(units, card, senior)}")
