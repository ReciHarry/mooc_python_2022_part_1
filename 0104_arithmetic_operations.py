# brief look at basic math used in Python.

# Learning Objectives
# You will be able to use variables in various arithmetic operations
# You will know how to deal with numbers in user input
# You will know how to cast values into other fundamental data types

# Operator	Purpose	                                 Example	    Result
# +	        Addition	                             2 + 4	        6
# -	        Subtraction	                             10 - 2.5	    7.5
# *	        Multiplication	                         -2 * 123	    -246
# /	        Division (floating point result)         9 / 2	        4.5
# //	    Division (integer result)	             9 // 2	        4
# %	        Modulo	                                 9 % 2	        1
# **	    Exponentiation	                         2 ** 3	        8

# operators = symbol. operand = number.
# the data type of an operand determines data type of the result.
# division is an exception however and will always result in a floating point number data type unless using // operator.
# integer result division will always round DOWN.
# you can force data types however like so:
# year = int(input("Which year were you born? ")) OR input_str = input("string") year = int(input_str)
# same can be done with float
# height = float(input("What is your height? "))

# Programming exercise: Times five
# Please write a program which asks the user for a number. 
# The program then prints out the number multiplied by five.

times_by_five = int(input("Please type in a number:"))
print(f"{times_by_five} times 5 is {times_by_five * 5}")

# Programming exercise: Name and age
# Please write a program which asks the user for their name and year of birth.

name = input("What is your name?")
birth_year = int(input("Which year were you born?"))
print(f"Hi {name}, you will be {2021-birth_year} years old at the end of the year 2021")

# sum += number is generally used to increase the value of a variable with each user input or a loop.
# moreover, only one variable is needed instead of 4 when dealing with 3 user inputs and calculating the sum.
# for example:

sum = 0

sum += int(input("First number: "))
sum += int(input("Second number: "))
sum += int(input("Third number: "))

print(f"The sum of the numbers: {sum}")

# sometimes we may need to have a cut off of how much we want to store, or what we want to increase. consider:

number1 = int(input("First number: "))
number2 = int(input("Second number: "))

print(f"{number1} + {number2} = {number1+number2}")

# Programming exercise: Seconds in a day
# Please write a program which asks the user for a number of days. 
# The program then prints out the number of seconds in the amount of days given.

days = int(input("How many days?"))
seconds_math = (24 * 60 * 60)
print(f"Seconds in that many days: {days*seconds_math}")

# Programming exercise: Fix the code: Product
# This program asks the user for three numbers. 
# The program then prints out their product, that is, the numbers multiplied by each other. 
# There is, however, something wrong with the program - it doesn't work quite right, 
# as you can see if you run it. Please fix it.

number = int(input("Please type in the first number: "))
number = number * int(input("Please type in the second number: "))
number = number * int(input("Please type in the third number: "))

print("The product is", number)

# Programming exercise: Sum and product
# Please write a program which asks the user for two numbers. 
# The program will then print out the sum and the product of the two numbers.

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
print(f"The sum of the numbers: {num1+num2}")
print(f"The product of the numbers: {num1*num2}")

# Programming exercise: Sum and mean
# Please write a program which asks the user for four numbers. 
# The program then prints out the sum and the mean of the numbers.

numb1 = int(input("Number 1"))
numb2 = int(input("Number 2"))
numb3 = int(input("Number 3"))
numb4 = int(input("Number 4"))
mean = float((numb1+numb2+numb3+numb4)/4)
print(f"The sum of the numbers is {numb1+numb2+numb3+numb4} and the mean is {mean}")

# using a sum variable would have made more sense with sum/4 as the mean in the f string in retrospect.
# being that the sum variable is far more versatile than the mean variable.

# Programming exercise: Food expenditure
# Please write a program which estimates a user's typical food expenditure. 
# The program asks the user how many times a week they eat at the student cafeteria. 
# Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

cafeteria_meals = int(input("How many times a week do you eat at the student cafeteria?"))
average_meal_price = float(input("The price of a typical student lunch?"))
weekly_shopping_price = float(input("How much money do you spend on groceries in a week?"))
weekly_overall = (cafeteria_meals * average_meal_price) + weekly_shopping_price
daily_overall = weekly_overall / 7

print("Average food expenditure:")
print(f"Daily: {daily_overall} euros")
print(f"Weekly: {weekly_overall} euros")

# Programming exercise: Students in groups
# Please write a program which asks for the number of students on a course and the desired group size. 
# The program will then print out the number of groups formed from the students on the course. 
# If the division is not even, one of the groups may have fewer members than specified.

total_students = int(input("How many students on the course?"))
desired_students = int(input("Desired group size?"))

if total_students % desired_students > 0:
    print(f"Number of groups formed: {(total_students // desired_students) + 1}")
else:
    print(f"Number of groups formed: {(total_students // desired_students)}")

# The given solution is as follows (without conditional statement)

students = int(input("How many students on the course? "))          # 8
group_size = int(input("Desired group size? "))                     # 4
 
groups = (students + group_size - 1) // group_size                  # 8+4-1 = 11 / 4 = 2.75, therefore 11 // 4 = 2 because it can only take the integer value.
 
print("Number of groups formed:", groups)                           # thus 2

# this is an interesting way to handle the problem