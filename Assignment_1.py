# QUESTION 1
print("Enter first number")
num1 = int(input())
print("Enter second number")
num2 = int(input())
print("Enter third number")
num3 = int(input())
print("The average of three numbers:\n",(num1+num2+num3)/3 )

print("\n\n")

# QUESTION 2
print("Enter your Gross income (to the nearest penny)")
Gross_income = int(input())
print("Enter the number of dependents")
Dependents = int(input())
Taxable_income = Gross_income-10000-(3000*Dependents)
print("Your Taxable income will be :\n", Gross_income-10000-(3000*Dependents))
print("Your tax is", Taxable_income*20/100, "\t(taxable income:", Taxable_income, ")")

print("\n\n")

# QUESTION 3
print("Enter your name")
_name = input()
print("Enter your SID")
_SID = input()
print("Enter your gender  (Male:M , Female:F , Unknown:U)")
_gender = input()
print("Enter course name  (use the specific abbreviation")
_course_name = input()
print("Enter your CGPA")
_CGPA = float(input())
YOUR_IDENTITY_CARD = [_SID, _name, _gender, _course_name, _CGPA]
print("YOUR IDENTITY CARD\t---->\t",YOUR_IDENTITY_CARD)

print("\n\n")

# QUESTION 4
print("Enter marks of Student1")
marks1 = float(input())
print("Enter marks of Student2")
marks2 = float(input())
print("Enter marks of Student3")
marks3 = float(input())
print("Enter marks of Student4")
marks4 = float(input())
print("Enter marks of Student5")
marks5 = float(input())
Students_marks = {"Student1":marks1, "Student2":marks2, "Student3":marks3, "Student4":marks4, "Student5":marks5,}
print("List of Students marks ----> ", Students_marks)

print("\n\n")

# QUESTION 5
List_of_colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
List_of_colors.remove('Black')
print(List_of_colors)
List_of_colors[3] = 'Purple'
print(List_of_colors)

