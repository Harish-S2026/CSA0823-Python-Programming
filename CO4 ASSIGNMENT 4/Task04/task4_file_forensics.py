"""
TASK 4 - Repaired library return log
Run: python task4_file_forensics.py
"""
from pathlib import Path
import tempfile

def save_returns(books, log_name="returns.log"):
    with open(log_name, "a", encoding="utf-8") as log_file:
        for book in books:
            book = book.strip()
            if book:
                log_file.write(book + "\\n")

def process(day_file, log_name="returns.log", error_log="errors.log"):
    try:
        with open(day_file, "r", encoding="utf-8") as source:
            books = source.read().splitlines()
        save_returns(books, log_name)
        return True
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError) as error:
        with open(error_log, "a", encoding="utf-8") as errors:
            errors.write(f"{day_file}: {type(error).__name__}: {error}\\n")
        return False

def demonstration():
    with tempfile.TemporaryDirectory() as folder:
        folder = Path(folder)
        log = folder / "returns.log"
        error_log = folder / "errors.log"
        for day, books in enumerate(
            (["Book A", "Book B"], ["Book C"], ["Book D", "Book E"]), start=1
        ):
            day_file = folder / f"day{day}.txt"
            day_file.write_text("\\n".join(books), encoding="utf-8")
            process(day_file, log, error_log)
        # Demonstrate missing-file handling.
        process(folder / "missing_day.txt", log, error_log)
        print("Combined return log:")
        print(log.read_text(encoding="utf-8"))
        print("Error log:")
        print(error_log.read_text(encoding="utf-8"))

if __name__ == "__main__":
    demonstration()
