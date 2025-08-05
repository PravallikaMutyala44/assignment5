# Create a dictionary with student names as keys and marks as values
student_marks = {
    "alice": 50,
    "bob": 75,
    "charlie": 90,
    "david": 60
}


name = input("Enter the student's name: ").lower()

if name in student_marks:
    print(f"{name.capitalize()}'s marks: {student_marks[name]}")
else:
    print("Student not found")
