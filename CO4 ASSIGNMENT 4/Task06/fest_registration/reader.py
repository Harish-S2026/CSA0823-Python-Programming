from .validator import validate_record

def read_department_file(path, error_log):
    valid_records = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    valid_records.append(validate_record(line))
                except ValueError as error:
                    error_log.append((str(path), line_number, str(error), line.strip()))
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError) as error:
        error_log.append((str(path), 0, type(error).__name__ + ": " + str(error), ""))
    return valid_records
