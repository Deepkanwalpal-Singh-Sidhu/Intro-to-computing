#Python Assignment 3.

#Q1

#Def a function to count the occurrence
def occurrence_counter(string):
    def character_counter(stng):
        output_list=[]
        for i in stng:
            count = stng.count(i)
            output_list.append("Number of occurrences of {} : {}\n".format(i,count))
        for o in set(output_list):
            print(o+"\n")
    def substring_counter(stn):
        for i in set(lst):
            print("Number of occurrences of", i,":", lst.count(i),"\n")
    lst = string.split()
    if len(lst)==1:
        character_counter(string)
    elif len(lst)==0:
        print("Empty String Input")
    else:
        substring_counter(string)
string1 = input("Input String:")
print()
occurrence_counter(string1)

#Q2

day = int(input("Please enter Date: "))
month = int(input("Please enter Month: "))
year = int(input("Please enter Year: "))
# Checking invalid cases and removing them
if day > 30 and month in {2, 4, 6, 9, 11}:
    condition = False
elif day > 31 and month in {1, 3, 5, 7, 8, 10, 12}:
    condition = False
elif (day == 29 or day == 30) and month == 2 and year % 4 != 0:
    condition = False
elif day == 30 and month == 2 and year % 4 == 0:
    condition = False
elif day <= 0 or month <= 0 or year > 2025 or year < 1800:
    condition = False
else:
    condition = True
#Using conditional statements to find next date.
if condition:
    if day == 31 and month == 12:
        next_year = year + 1
    else:
        next_year = year
    if month == 12 and day == 31:
        next_month = 1
    else:
        next_month = month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day == 31:
            next_day = 1
            if month != 12:
                next_month = month + 1
            else:
                next_month = 1
        else:
            next_day = day + 1
    elif month == 2:
        if year % 4 == 0:
            if day == 29:
                next_day = 1
                next_month = 3
            else:
                next_day = day + 1
        else:
            if day == 28:
                next_day = 1
                next_month = 3
            else:
                next_day = day + 1
    else:
        if day == 30:
            next_day = 1
            next_month = month + 1
        else:
            next_day = day + 1
    print(f"Next Date is: {next_day}/{next_month}/{next_year}")
else:
    print("That's not a valid date")

#Q3

#Initial list of numbers
num = [3,9,10]

output_list = []
#using for loop to make the list of tuples containing the squares
for i in num:
    output_list.append((i, i ** 2))

print()
print(output_list)
print()
print()

#Q4

grade=int(input("Enter Grade Points: "))

#Storing the given table in a dictionary
grade_table ={10:{'grade_input':'A+','remarks':'Outstanding'},
           9:{'grade_input':'A','remarks':'Excellent'},
           8:{'grade_input':'B+','remarks':'Very Good'},
           7:{'grade_input':'B','remarks':'Good'},
           6:{'grade_input':'C+','remarks':'Average'},
           5:{'grade_input':'C','remarks':'Below Average'},
           4:{'grade_input':'D','remarks':'Poor'}}

if 3<grade<11:
    for key in grade_table.keys():
        if key == grade:
            value = grade_table[key]
            print(f"Your Grade is {value['grade_input']} and {value['remarks']} performance ")
        else:
            continue
else:
    print("Error! You entered an invalid grade")

print()
#Q5

#list from A to K.
chr_lst = ['A','B','C','D','E','F','G','H','I','J','K']

# Printing out the pattern.
while len(chr_lst) >= 1:
    print((''.join(chr_lst)).center(11, ' '))
    if len(chr_lst)==1:
        chr_lst.pop()
    else:
        chr_lst.pop(-1)
        chr_lst.pop(-1)
print()

#Q6

condition=True
#Defining dictionary to store the values
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        name=input("Please enter the name of the Student: ")
        SID = int(input("Please Enter SID of Student: "))
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N: ")
        condition = True
    else:
        condition = False
for key,value in Dictionary.items():
    print(f"{key} : {value}")
Val_sort_dict= sorted(Dictionary.values())
Name_sort = {}
def get_key(val, dicti):
    for key, value in dicti.items():
        if val == value:
            return key
for s_name in Val_sort_dict:
    s_sid = get_key(s_name, Dictionary)
    Name_sort[s_sid] = s_name
print(Name_sort)
Key_sort_dict= sorted(Dictionary.keys())
dict={}
for i in Key_sort_dict:
    dict[i]=Dictionary[i]
print(dict)
sid=int(input("Please enter the student's SID whose detail you need: "))
if sid in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[sid]}")
else:
    print("The SID is not present in the given Data")
print()

#Q7

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n <= 0:
        return "\nError!: Number of terms can not be -ve or 0."
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter the number of terms of fibonacci sequence you want:"))

sequence_list = []
for t in range(1, num + 1):
    sequence_list.append(fibonacci(t))


print(f"\nFirst {num} terms of fibonacci sequence are:", end=' ')

for i in sequence_list:
    print(i, end=' ')

# Finding out the average of the printed our fibonacci series.
avg = sum(sequence_list) / num
print("\nThe average of the resultant fibonacci series is:", avg)
print()

#8 

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#a
set_a=Set1^Set2
print("Part a",set_a)

#b
set_b=Set1^Set2^Set3
print("Part b",set_b)

#c
set_c=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print("Part c",set_c)

#d
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
set_d=new_set1- Set1
print("Part d", set_d)

#e
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
set_e=new_set2 - (Set1|Set2|Set3)
print("Part e",set_e)
