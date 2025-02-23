import json

# Define the JSON file name
json_file = "students.json"

# Function to print student list
def print_students(students, message):
    print("\n" + message)
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load the JSON data
try:
    with open(json_file, "r") as file:
        students = json.load(file)
except FileNotFoundError:
    print(f"Error: {json_file} not found.")
    students = []

# Print original student list
print_students(students, "Original Student List:")

# Append new student (Your details)
new_student = {
    "F_Name": "Austin",
    "L_Name": "Wiant",  # Replace with your actual last name
    "Student_ID": 19709,  # Fictional ID
    "Email": "awiant@gmail.com"  # Replace with a fictional email
}
students.append(new_student)

# Print updated student list
print_students(students, "Updated Student List:")

# Save updated list back to JSON file
with open(json_file, "w") as file:
    json.dump(students, file, indent=4)

print("\nThe students.json file has been updated.")
