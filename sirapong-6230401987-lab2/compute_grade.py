def check(score):
    if score.isdigit():
        score = int(score)
        if score >= 0 and score <= 100:
            return True
        else:
            return False
    else:
        return False


student_name = str(input("Please enter a student name: "))
while True:

    midterm_exam = input("Please enter the student's midterm exam mark (0-100): ")

    if check(midterm_exam) == True:
        break
    else:
        print("Please enter a valid exam mark (0-100)")

while True:

    final_exam = input("Please enter the student's final exam mark (0-100): ")
    if check(final_exam) == True:
        break
    else:
        print("Please enter a valid exam mark (0-100)")

sum = int(midterm_exam) + int(final_exam)
average = sum / 2

if average >= 80 and average <= 100:
    print(student_name, "has total mark as %.2f and grade as A" % average)
elif average >= 70 and average <= 79:
    print(student_name, "has total mark as %.2f and grade as B" % average)
elif average >= 60 and average <= 69:
    print(student_name, "has total mark as %.2f and grade as C" % average)
elif average >= 50 and average <= 59:
    print(student_name, "has total mark as %.2f and grade as D" % average)
elif average <= 49:
    print(student_name, "has total mark as %.2f and grade as F" % average)
