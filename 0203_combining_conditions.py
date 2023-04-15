# putting two or more conditions into a statement

# Learning Objectives
# You will know how to use the operators and, or and not in conditions
# You will be able to write nested conditionals

# The condition number >= 5 and number <= 8 determines that number must simultaneously be at least 5 and at most 8. 
# That is, it must be between 5 and 8.

number = int(input("Please type in a number: "))
if number >= 5 and number <= 8:
    print("The number is between 5 and 8")

# Meanwhile, the condition number < 5 or number > 8 determines that number must be either less than 5 or greater than 8. 
# That is, it must not be within the range of 5 to 8.

number = int(input("Please type in a number: "))
if number < 5 or number > 8:
    print("The number is not within the range of 5 to 8")

# Sometimes it is necessary to know if something is not true. The operator not negates a condition:

number = int(input("Please type in a number: "))
if not (number >= 5 and number <= 8):
    print("The number is not within the range of 5 to 8")

# The condition:

# x >= a and x <= b 

# is a very common way of checking whether the number x falls within the range of a to b. 
# An expression with this structure works the same way in most programming languages.

# Python also allows a simplified notation for combining conditions: 
# a <= x <= b 
# achieves the same result as the longer version using "and"

# This shorter notation might be more familiar from mathematics, 
# but it is not very widely used in Python programming, 
# possibly because very few other programming languages have a similar shorthand.

# The following program asks the user to type in four numbers. 
# It then works out which of the four is the greatest, with the help of some conditions:

n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
elif n2 > n3 and n2 > n4:
    greatest = n2
elif n3 > n4:
    greatest = n3
else:
    greatest = n4

print(f" {greatest} is the greatest of the numbers.")

# Programming exercise: Age check
# Please write a program which asks for the user's age. 
# If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.

age = int(input("What is your age? "))

if age >= 5:
    print(f"Ok, you're {age} years old")
elif age < 5 and age >= 0:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")

# Programming exercise: Nephews
# Please write a program which asks for the user's name. 
# If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.
# In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

username = input("Please type in your name: ")

if username == "Huey" or username == "Dewey" or username == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif username == "Morty" or username == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# Programming exercise: Grades and points
# The table below outlines the grade boundaries on a certain university course. 
# Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

score = int(input("How many points [0-100]: "))

if score < 0:
    print("Grade: impossible!")
elif score < 50:
    print("Grade: fail")
elif score < 60:
    print("Grade: 1")
elif score < 70:
    print("Grade: 2")
elif score < 80:
    print("Grade: 3")
elif score < 90:
    print("Grade: 4")
elif score <= 100:
    print("Grade: 5")
else:
    print("Grade: impossible!")

# "if score < 0 or points > 100:" would have been better

# Programming exercise: FizzBuzz
# Please write a program which asks the user for an integer number. 
# If the number is divisible by three, the program should print out Fizz. 
# If the number is divisible by five, the program should print out Buzz. 
# If the number is divisible by both three and five, the program should print out FizzBuzz.

divisible = int(input("Number: "))

if divisible % 3 == 0 and divisible % 5 == 0:
    print("FizzBuzz")
elif divisible % 3 == 0:
    print("Fizz")
elif divisible % 5 == 0:
    print("Buzz")

# Nested conditionals
# Conditional statements can also be nested within other conditional statements. 
# For example, the following program checks whether a number is above zero, and then whether it is odd or even:

number = int(input("Please type in a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")

# With nested conditional statements it is crucial to get the indentations right. 
# Indentations determine which branches are linked together.

# The same result can often be achieved using either nested conditional statements or conditions combined with logical operators.

number = int(input("Please type in a number: "))

if number > 0 and number % 2 == 0:
    print("The number is even")
elif number > 0 and number % 2 != 0:
    print("The number is odd")
else:
    print("The number is negative or zero")

# Neither approach is intrinsically better than the other, but in different situations one or the other may seem more logical. 
# In this particular example most people tend to find the first version with nesting to be more intuitive.

# Programming exercise: Leap year
# Generally, any year that is divisible by four is a leap year. 
# However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.
# Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

year = int((input("Please type in a year: ")))

if year % 100 == 0:
    if year % 400 == 0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# alternatively:

year = int(input("Please type in a year: "))
 
# First, we make assumption that a year is not a leap year
leap_year = False
 
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True
 
if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# Programming exercise: Alphabetically in the middle
# Please write a program which asks the user for three letters. 
# The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
# You may assume the letters will be either all uppercase, or all lowercase.

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter1 > letter2 and letter1 > letter3:
    if letter2 > letter3:
        print(f"The letter in the middle is {letter2}")
    else:
        print(f"The letter in the middle is {letter3}")
elif letter2> letter3 and letter2 > letter1:
    if letter1 > letter3:
        print(f"The letter in the middle is {letter1}")
    else:
        print(f"The letter in the middle is {letter3}")
else:
    if letter1 > letter2:
        print(f"The letter in the middle is {letter1}")
    else:
        print(f"The letter in the middle is {letter2}")

# Programming exercise: Gift tax calculator
# Please write a program which calculates the correct amount of tax for a gift from a close relative. 
# Have a look at the examples below to see what is expected. 
# Notice the lack of thousands separators in the input values - you may assume there will be 
# no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.

gift_tax = int(input("Value of gift: "))

if gift_tax > 1000000:
    print(f"Amount of tax: {(142100 + (gift_tax - 1000000) * 0.17)} euros")
elif gift_tax > 200000:
    print(f"Amount of tax: {(22100 + (gift_tax - 200000) * 0.15)} euros")
elif gift_tax > 55000:
    print(f"Amount of tax: {(4700 + (gift_tax - 55000) * 0.12)} euros")
elif gift_tax > 25000:
    print(f"Amount of tax: {(1700 + (gift_tax - 25000) * 0.1)} euros")
elif gift_tax > 5000:
    print(f"Amount of tax: {(100 + (gift_tax - 5000) * 0.08)} euros")
else:
    print("No tax!")