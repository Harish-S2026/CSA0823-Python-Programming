from pathlib import Path
from fest_registration.processor import process_files

if __name__ == "__main__":
    # Demo folder and files are created so the test can run immediately.
    input_folder = Path("sample_input")
    output_folder = Path("output")
    input_folder.mkdir(exist_ok=True)

    (input_folder / "ece.txt").write_text(
        "R001,Asha,ECE,asha@example.com,Robotics;AI\\n"
        "R002,Bala,ECE,bala@example.com,AI\\n"
        "R003,Chitra,ECE,wrong-email,Robotics\\n"
        "R004,Devi,ECE,devi@example.com\\n",
        encoding="utf-8"
    )
    (input_folder / "cse.txt").write_text(
        "R001,Asha,ECE,asha@example.com,Robotics\\n"
        "R005,Eshan,CSE,eshan@example.com,Cybersecurity\\n",
        encoding="utf-8"
    )
    # mech.txt is intentionally absent to demonstrate missing-file handling.
    master, events, errors = process_files(
        input_folder, output_folder, ["ece.txt", "cse.txt", "mech.txt"]
    )
    print("Unique registrations:", len(master))
    print("Events:", sorted(events))
    print("Errors logged:", len(errors))
    print("Check the output folder for generated reports.")
