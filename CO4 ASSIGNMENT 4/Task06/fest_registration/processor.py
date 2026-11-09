from pathlib import Path
from .reader import read_department_file

def process_files(input_folder, output_folder, department_files):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    errors = []
    master = {}
    for file_name in department_files:
        records = read_department_file(input_folder / file_name, errors)
        for record in records:
            register = record["register"]
            if register in master:
                errors.append((file_name, 0, "duplicate registration", register))
                continue
            master[register] = record

    event_lists = {}
    for record in master.values():
        for event in record["events"]:
            event_lists.setdefault(event, []).append(record)

    # Master list
    with (output_folder / "master_list.csv").open("w", encoding="utf-8") as file:
        file.write("Register,Name,Department,Email,Events\\n")
        for record in sorted(master.values(), key=lambda x: x["register"]):
            file.write(
                f'{record["register"]},{record["name"]},{record["department"]},'
                f'{record["email"]},{";".join(record["events"])}\\n'
            )

    # Event-wise lists
    for event, records in event_lists.items():
        safe_name = "".join(ch if ch.isalnum() else "_" for ch in event)
        with (output_folder / f"event_{safe_name}.csv").open("w", encoding="utf-8") as file:
            file.write("Register,Name,Department,Email\\n")
            for record in records:
                file.write(
                    f'{record["register"]},{record["name"]},'
                    f'{record["department"]},{record["email"]}\\n'
                )

    with (output_folder / "summary_report.txt").open("w", encoding="utf-8") as file:
        file.write(f"Total unique registrations: {len(master)}\\n")
        file.write(f"Total events: {len(event_lists)}\\n")
        for event, records in sorted(event_lists.items()):
            file.write(f"{event}: {len(records)} participants\\n")

    with (output_folder / "error_log.txt").open("w", encoding="utf-8") as file:
        for item in errors:
            file.write(" | ".join(map(str, item)) + "\\n")

    return master, event_lists, errors
