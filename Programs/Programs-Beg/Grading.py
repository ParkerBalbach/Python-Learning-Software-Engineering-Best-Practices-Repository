

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    "Random": 50,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
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


print(student_grades)