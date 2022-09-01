# class average

total = 0
grade_counter = 1
while grade_counter <= 10:
    grade = int(input("Please enter next grade:"))
    total = total + grade
    grade_counter = grade_counter + 1
class_avarage = total / 1012
print("Class avarage is", class_avarage)