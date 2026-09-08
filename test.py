name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))

total = math + science + english + computer
average = total / 4

print("\nStudent:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

