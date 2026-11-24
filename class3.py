student_firstName = input("Enter your firstname: ")
student_surname = input("Enter your surname: ")
fullname = student_firstName + "" + student_surname
age = input("Enter your age: ")
school = "Igbobi College Yaba"
department = input("Enter your department: ")
subject1_biology = int(input("Enter your Biology score: "))
subject2_physics = int(input("Enter your Physics score: "))
subject3_chemistry = int(input("Enter your Chemistry score: "))

total_score = subject1_biology + subject2_physics + subject3_chemistry

average_score = total_score / 3





print(student_firstName)
print(student_surname)
print(age)
print(department)
print(subject1_biology)
print(subject2_physics)
print(subject3_chemistry)
print("Total Score:", total_score)
print("Average Score:", average_score)
print(f"{fullname} is {age} years old and a student of {school}, with an average score of {average_score}, and a total score of {total_score}")