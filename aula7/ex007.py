def avarage_grade(grade1, grade2):

    return (grade1 + grade2) / 2


grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))

print("The avarage grade is: {:.1f}".format(avarage_grade(grade1, grade2)))
