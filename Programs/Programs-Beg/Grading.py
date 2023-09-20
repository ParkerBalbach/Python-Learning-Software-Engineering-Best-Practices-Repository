# Predefine a dictionary containing student names as keys and their respective scores as values
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    "Random": 50,
}

# Initialize an empty dictionary to store student grades
student_grades = {}

# Iterate through each student and their corresponding score
for student in student_scores:
    score = student_scores[student]
    
    # Determine the grade based on the score
    if score >= 90:
        student_grades[student] = 'A'
    elif score >= 80:
        student_grades[student] = 'B'
    elif score >= 70:
        student_grades[student] = 'C'
    elif score >= 60:
        student_grades[student] = 'D'
    elif score < 60:
        student_grades[student] = 'F'

# Print the resulting dictionary with student names and their corresponding grades
print(student_grades)
