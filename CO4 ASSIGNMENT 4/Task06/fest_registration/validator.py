def validate_record(line):
    fields = [item.strip() for item in line.strip().split(",")]
    if len(fields) != 5:
        raise ValueError(f"expected 5 comma-separated fields, found {len(fields)}")
    register, name, department, email, events_text = fields
    if not register or not name or not department:
        raise ValueError("register number, name and department are required")
    if "@" not in email or "." not in email.split("@")[-1] or email.startswith("@"):
        raise ValueError("invalid e-mail address")
    events = [event.strip() for event in events_text.split(";") if event.strip()]
    if not events:
        raise ValueError("at least one event is required")
    return {
        "register": register,
        "name": name,
        "department": department,
        "email": email,
        "events": events
    }
