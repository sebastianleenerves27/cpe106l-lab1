student = {
    "id": "2025-001",
    "name": "Juan Dela Cruz",
    "grades": [88, 90, 85]
}

def calculate_average(grades):
    return sum(grades) / len(grades)

print("Activity 1: Student Average")
print(f"Student ID: {student['id']}")
print(f"Name: {student['name']}")
print(f"Grades: {student['grades']}")
print(f"Average Grade: {calculate_average(student['grades']):.2f}")
print("\n" + "-"*40 + "\n")

new_name = input("Enter updated student name (leave blank to keep current): ").strip()
if new_name:
    student["name"] = new_name

while True:
    try:
        new_grade = input("Enter a new grade to add (or 'done' to finish): ").strip()
        if new_grade.lower() == 'done':
            break
        new_grade = float(new_grade)
        if 0 <= new_grade <= 100:
            student["grades"].append(new_grade)
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Enter a number or 'done'.")

print("\nActivity 2: Updated Student Record")
print(f"Student ID: {student['id']}")
print(f"Name: {student['name']}")
print(f"Grades: {student['grades']}")
print(f"New Average Grade: {calculate_average(student['grades']):.2f}")

