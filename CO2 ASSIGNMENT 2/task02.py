# Q2 - OTP verification: while, for, loop-else and recursion
CORRECT_OTP = "482913"

def verify_while(entries, correct=CORRECT_OTP):
    attempts = 0
    for entered in entries:
        if entered == "":
            print("Blank entry: not counted")
            continue
        attempts += 1
        if entered == correct:
            print("OTP accepted")
            break
        print("Incorrect OTP")
        if attempts == 3:
            print("Account locked for 30 minutes")
            break
    return attempts

def verify_for(entries, correct=CORRECT_OTP):
    # The for loop is bounded to three nonblank attempts.
    attempts = 0
    iterator = iter(entries)
    for _ in range(3):
        entered = next(iterator, None)
        while entered == "":
            print("Blank entry: not counted")
            entered = next(iterator, None)
        if entered is None:
            break
        attempts += 1
        if entered == correct:
            print("OTP accepted")
            break
        print("Incorrect OTP")
    else:
        print("Account locked for 30 minutes")
    return attempts

def verify_with_security(entries, security_answer, correct_answer,
                         correct=CORRECT_OTP):
    limit = 3 + (2 if security_answer.strip().lower()
                 == correct_answer.strip().lower() else 0)
    attempts = 0
    for entered in entries:
        if entered == "":
            continue
        attempts += 1
        if entered == correct:
            print("OTP accepted")
            break
        if attempts == limit:
            print("Account locked for 30 minutes")
            break
    return attempts

def verify_recursive(entries, index=0, attempts=0, correct=CORRECT_OTP):
    if attempts >= 3 or index >= len(entries):
        return "Locked / no more attempts", attempts
    entered = entries[index]
    if entered == "":
        return verify_recursive(entries, index + 1, attempts, correct)
    if entered == correct:
        return "OTP accepted", attempts + 1
    return verify_recursive(entries, index + 1, attempts + 1, correct)

if __name__ == "__main__":
    print("WHILE")
    verify_while(["", "111111", "222222", "333333"])
    print("\\nFOR")
    verify_for(["", "111111", "222222", "333333"])
    print("\\nSecurity question gives five attempts")
    verify_with_security(["1", "2", "3", "4", "482913"], "blue", "blue")
    print("\\nRecursive:", verify_recursive(["", "1", "2", "482913"]))
    # pass is a syntactically valid no-operation placeholder, e.g.:
    if False:
        pass
