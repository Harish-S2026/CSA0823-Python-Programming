# 1. Student's roll number
roll_number = int(input("Enter roll number: "))

# 2. Marks in 5 subjects
marks = []
for i in range(5):
    mark = float(input("Enter mark: "))
    marks.append(mark)

# 3. Days of the week
days = tuple(input("Enter days of the week: ").split())

# 4. Unique email IDs of club members
email_ids = set(input("Enter email IDs separated by spaces: ").split())

# 5. Student's name, age and class
name = input("Enter student name: ")
age = int(input("Enter age: "))
student_class = input("Enter class: ")

student = {
    "name": name,
    "age": age,
    "class": student_class
}

# 6. Whether a library book is issued
book_issued = input("Is the book issued? (True/False): ") == "true"

print("\n--- Student Details ---")
print("Roll number =", roll_number)
print("Marks =", marks)
print("Days =", days)
print("Email IDs =", email_ids)
print("Student =", student)
print("Book issued =", book_issued)