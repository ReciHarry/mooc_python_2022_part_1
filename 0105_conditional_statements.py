# brief look into conditional statements.

# Learning Objectives
# You will be able to use a simple conditional statement in programming
# You will know what a Boolean value is
# You will be able to express conditionals with comparison operators

# Operator      Purpose	                    Example
# ==	        Equal to	                a == b
# !=	        Not equal to	            a != b
# >	            Greater than	            a > b
# >=	        Greater than or equal to	a >= b
# <	            Less than	                a < b
# <=	        Less than or equal to	    a <= b

# example of conditional statement in python:

password = input("Please type in a password: ")

if password == "kittycat":
    print("You knew the password!")
    print("You must be either the intended user...")
    print("...or quite an accomplished hacker.")

print("The program has finished its execution. Thanks and bye!")

# Programming exercise: Orwell
# Please write a program which asks the user for an integer number. 
# The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

year = int(input("Please type in a number:"))
if year == 1984:
    print("Orwell")

# Programming exercise: Absolute value
# Please write a program which asks the user for an integer number. 
# If the number is less than zero, the program should print out the number multiplied by -1. 
# Otherwise the program prints out the the number as is.

is_it_negative = int(input("Please type in a number:"))
if is_it_negative < 0:
    print(f"The absolute value of this number is {is_it_negative * -1}")
else:
    print(f"The absolute value of this number is {is_it_negative}")

# alternatively can be written like this:

is_number_negative = int(input("Please type in a number: "))
absolute_value = is_number_negative
if is_number_negative < 0:
    absolute_value = is_number_negative * -1
print("The absolute value of this number is", absolute_value)

# Programming exercise: Soup or no soup
# Please write a program which asks for the user's name. 
# If the name is anything but "Jerry", the program then asks for the number of portions 
# and prints out the total cost. The price of a single portion is 5.90.

customer_name = input("Please tell me your name:")
if customer_name != "Jerry":
    customer_portions = int(input("How many portions of soup?"))
    print(f"The total cost is {5.90*customer_portions}")

print("Next please!")

# the test passed but the result of 3*5.90 is coming up as "The total cost is 17.700000000000003" for some reason?

# Programming exercise: Order of magnitude
# Please write a program which asks the user for an integer number. 
# The program should then print out the magnitude of the number according to the following examples.

user_number = int(input("Please type in a number:"))
if user_number < 1000:
    print("This number is smaller than 1000")
if user_number < 100:
    print("This number is smaller than 100")
if user_number < 10:
    print("This number is smaller than 10")

print("Thank you!")

# boolean / bool values pertain to true or false statements within python. For example:

a = 3
condition = a < 5
print(condition)
if condition:
    print("a is less than 5")

# Sample output:
# True
# a is less than 5

# Programming exercise: Calculator
# Please write a program which asks the user for two numbers and an operation. 
# If the operation is add, multiply or subtract, the program should calculate 
# and print out the result of the operation with the given numbers. 
# If the user types in anything else, the program should print out nothing.

# I will execute this with booleans just for the sake of rehearsal.

user_num1 = int(input("Number 1:"))
user_num2 = int(input("Number 2:"))
user_operator = input("Operation:")

add = user_operator == "add"
multiply = user_operator == "multiply"
subtract = user_operator == "subtract"

if add:
    print(f"{user_num1} + {user_num2} = {user_num1 + user_num2}")
if multiply:
    print(f"{user_num1} * {user_num2} = {user_num1 * user_num2}")
if subtract:
    print(f"{user_num1} - {user_num2} = {user_num1 - user_num2}")

# Programming exercise: Temperatures
# Please write a program which asks the user for a temperature in degrees Fahrenheit, 
# and then prints out the same in degrees Celsius. If the converted temperature 
# falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".
# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

temperature_f = int(input("Please type in a temperature (F)"))
temperature_c = (temperature_f - 32) * 5 / 9
print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")
if temperature_c < 0:
    print("Brr! It's cold in here!")

# Programming exercise: Daily wages
# Please write a program which asks for the hourly wage, 
# hours worked, and the day of the week. The program should 
# then print out the daily wages, which equal hourly wage multiplied 
# by hours worked, except on Sundays when the hourly wage is doubled.

hourly_wage = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
day_of_week = input("Day of the week:")
if day_of_week != "Sunday":
    print(f"Daily wages: {hourly_wage*hours_worked} euros")
else:
    print(f"Daily wages: {hourly_wage*2*hours_worked} euros")

# Programming exercise: Loyalty bonus
# This program calculates the end of year bonus a customer receives on their loyalty card.

points = int(input("How many points are on your card? "))

if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

print("You now have", points, "points")

# I just switched the conditional statements' positions around because previously the *= 1.1 was multiplying the points operand to 100 or more.
# The suggested formula is as follows:

points = int(input("How many points are on your card? "))
if points < 100:
    factor = 1.1
    print("Your bonus is 10 %")
    
if points >= 100:
    factor = 1.15
    print("Your bonus is 15 %")
 
# a *= b is the same thing as a = a * b
points *= factor
print("You now have", points, "points")

# Programming exercise: What to wear tomorrow
# Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.
# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")

if temperature <= 20:
    print("I recommend a jumper as well")

if temperature <= 10:
    print("Take a jacket with you")

if temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!")

# Programming exercise: Solving a quadratic equation
# In the Python math module there is the function sqrt, 
# which calculates the square root of a number. You can use it like so:

# from math import sqrt
# print(sqrt(9))

# Sample Output: 3.0

# We will return to the concept of a module and the import statement later. 
# For now, it is sufficient to understand that the line from math import sqrt allows us to use the sqrt function in our program.
# Please write a program for solving a quadratic equation of the form ax²+bx+c. 
# The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. 
# The quadratic formula expressed with the Python sqrt function is as follows:
# x = (-b ± sqrt(b²-4ac))/(2a).
# You can assume the equation will always have two real roots, so the above formula will always work.

# sqrt(9) is equivalent to 9 ** 0.5

from math import sqrt

a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))
discriminant = b ** 2 - 4 * a * c
x = float((-b + sqrt(discriminant)) / (2 * a))
y = float((-b - sqrt(discriminant)) / (2 * a))

print(f"The roots are {x} and {y}")

# made a lot of mistakes with this but ultimately didn't have paranthesis tagged around -b to sqrt(d)