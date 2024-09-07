#intialize the valude of student name, final quizzes, final research, final project, final exam ratings

student_name = ""
final_quizzes = 0
final_research = 0
final_project = 0
final_exam = 0
grade_remark = ""

#input student name, final quizzes, final research, final project, final exam ratings

student_name = input("Enter student's name: ")
final_quizzes = float(input("Enter final quizzes rating (0-100): "))
final_research = float(input("Enter final research/assignment rating (0-100): "))
final_project = float(input("Enter final project rating (0-100): "))
final_exam = float(input("Enter final exam rating (0-100)"))

#setting the formula for the final grade

final_grade = (0.30 * final_quizzes) + (0.10 * final_research) + (0.40 * final_project) + (0.20 * final_project)

#determine the final grade based on the numerical value obtained by the following grading remarks

if 98 <= final_grade <= 100:
    grade_remark = 4.00
elif 95 <= final_grade <= 97:
    grade_remark = 3.75
elif 92 <= final_grade <= 94:
    grade_remark = 3.50
elif 89 <= final_grade <= 91:
    grade_remark = 3.25
elif 86 <= final_grade <= 88:
    grade_remark = 3.00
elif 83 <= final_grade <= 85:
    grade_remark = 2.75
elif 80 <= final_grade <= 82:
    grade_remark = 2.50
elif 77 <= final_grade <= 79:
    grade_remark = 2.00
elif 74 <= final_grade <= 76:
    grade_remark = 1.75
elif 71 <= final_grade <= 73:
    grade_remark = 1.50
elif 68 <= final_grade <= 70:
    grade_remark = 1.25
elif 60 <= final_grade <= 63:
    grade_remark = 1.00
else:
    grade_remark = 0.00

#display student name, final quizzes, final research, final project, final exam, final grade, and equivalent mark

print("Student Name", student_name)
print("Final quizzes", final_quizzes)
print("Final research", final_research)
print("Final project", final_project)
print("Final Exam", final_exam)
print("Final grade", final_grade)
print("Grade mark", grade_remark)