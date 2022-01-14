#assignment 1 of python
#ques 1
num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:"))
num3=float(input("Enter 3rd number:"))

#calculating average for the 3 numbers
Average=(num1+num2+num3)/3

#printing average of the 3 numbers
print("The average of 3 numbers is:",Average)

#ques2
print()
Gross_income=float(input("Enter the gross income:"))
Dependents=int(input("Enter number of dependents:"))

#tax rate=20%
#standard deduction=$10000
#additional dependent deduction=$3000

#calcuating taxable income
Taxable_income=Gross_income-10000-(Dependents*3000)
#calculating the person's income tax
Tax=Taxable_income*(20/100)

#printing the person's income tax
print("Total tax calculated is:",Tax)                         

#ques3
print()
#making a list of details of student
Student=[21104117,"Deepkanwalpal Singh Sidhu","M","Intro to computing",9.4]

#printing the list made
print("Student",Student)

#ques4
print()

STU1=float(input("Enter marks of 1st student:"))
STU2=float(input("Enter marks of 2nd student:"))
STU3=float(input("Enter marks of 3rd student:"))
STU4=float(input("Enter marks of 4th student:"))
STU5=float(input("Enter marks of 5th student:"))

#STU represents student
#making a list of marks entered
Marks=[STU1,STU2,STU3,STU4,STU5]
#sorting the list
Marks.sort()
#printing the list in a sorted manner
print("Marks",Marks)

#ques5
print()
Color=["Red","Green","White","Black","Pink","Yellow"]

#ques5,part a
#removing the 4th element from the given list,and 3 is written because it is index of 4th element
Color.pop(3)

#printing the list with desired elements
print("Color",Color)

#ques5,part b
print()
Color=["Red","Green","White","Black","Pink","Yellow"]
#removing 4th and 5th element and replacing with purple
Color[3:5]=["Purple"]
#printing the list with the change made
print("Color",Color)
