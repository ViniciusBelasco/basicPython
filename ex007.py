def avarage_grade(grade1, grade2):

    return (grade1 + grade2) / 2


grade1 = int(input("Enter the first grade: "))
grade2 = int(input("Enter the second grade: "))

print("The avarage grade is: {:.1f}".format(avarage_grade(grade1, grade2)))
