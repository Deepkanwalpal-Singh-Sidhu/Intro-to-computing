#assignment-2

#ques1

#printing the input string just for reference
x="Python is a case sensitive language"
print(x)

#part a.
print('a.',"The length of the input string is:",len(x))

#part b.
print('b.',x[::-1])

#part c.
print('c.',x[10 : 26])

#part d.
#using.replace to get our required output
print("d.", x.replace("a case sensitive","object oriented"))

#part e.
print("e.", x.find("a"))


#ques2
print()
#storing my data into different variables
Name="Deepkanwalpal Singh Sidhu"
SID= "21104117"
Branch="Electrical"
CGPA="9.2"

print("Hey {0} Here! \nMy SID is {1} \nI am from {2} and my CGPA is{3}".format(Name,SID,Branch,CGPA))

#ques3
print()

a=56
b=10

#part a.
print('a.', a&b)

#part b.
print('b.', a|b)

#part c
print('c.', a^b)

#part d
#ledt shifting both a and b with 2 bits
print('d.', a<<2 ,"and", b<<2)

#part e
#right shifting a with 2 bits and b with 4 bits
print('e.', a>>2, "and", b>>4)

#ques 4
print()
#taking 3 numbers as input from user
num1=float(input("Enter the 1st number:",))
num2=float(input("Enter the 2nd number:",))
num3=float(input("Enter the 3rd number:",))

#using if esle
if (num1>=num2) and (num1>=num3) :
    print("num1 is the largest number")
elif (num2>=num3) and (num2>=num1) :
    print("num2 is the largest number")
else :
    print("num3 is the largest number")
    
#ques 5
print()    
#taking data from user
data_from_user=str(input())

print(data_from_user)

#using if else now

if 'name' in data_from_user:
    print("Yes")
else :
    print("No")

#ques 6
print()
#taking sides of triangles as input from user
x=int(input("Length of side 1 is:",))
y=int(input("Length of side 2 is:",))
z=int(input("Length of side 3 is:",))

#if any of the 3 lengths is greater than sum of other 2,triangle can not be formed

#using if else

if x+y>z and y+z>x and z+x>y :
    print("Yes,triangle can be formed")
else :
    print("No,triangle can not be formed")
