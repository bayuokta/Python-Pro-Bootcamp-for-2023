student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
def score_criteria(score:int)->str:
    if score >= 91:
        return 'Outstanding'
    elif score >= 81:
        return 'Exceeds Expectations'
    elif score >= 71:
        return 'Acceptable'
    else:
        return 'Fail'

for key, value in student_scores.items():
    student_grades[key] = score_criteria(value)


# 🚨 Don't change the code below 👇
print(student_grades)