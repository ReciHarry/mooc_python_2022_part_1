# understanding basic central concepts in programming.

# Learning Objectives
# You will be familiar with some essential terminology in programming
# You will know the difference between a statement and an expression
# You will be able to find out the data type of an evaluated expression
# You will have learnt to use debugging methods to find mistakes in your code

# statement = part of the program which executes something. usually refers to a single command. example = print("hi!") or number = 2
# block = group of consecutive statements that are teh same level in the structure of the program
# expression = code which results in a determined data type. example - 2 + 4 + 3 or "abc" + "de" provide the values 9 and abcde
# because expressions have a type, they can be assigned to variables
# function = executes some functionality. can also take one or more arguments or parameters. a function is executed when it is called
# for example the statement print("this is an argument") calls the function print with the argument "this is an argument"
# data type = boolean / integer / string etc
# syntax = language determines how the code of a program should be written
# debugging = if syntax is correct but program isn't functioning as intended, there is a bug in the program

# adding debugging print statements to code is an effective way to debug a program.
# the following is an attempt to solve one of the exercises from the previous section:

hourly_wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

daily_wages = hourly_wage * hours
if day == "sunday":
    daily_wages * 2

print(f"Daily wages: {daily_wages} euros")

# debugging means running a program multiple times. 
# it's often better to "hard-code" the problematic input rather than constantly re-ask for user input.
# hard-coding can look like this

# hourly_wage = float(input("Hourly wage: "))
# hours = int(input("Hours worked: "))
# day = input("Day of the week: ")
hourly_wage = 20.0
hours = 6
day = "Sunday"

daily_wages = hourly_wage * hours
if day == "sunday":
    daily_wages * 2

print(f"Daily wages: {daily_wages} euros")

# and then by adding debugging print statements

# ...

daily_wages = hourly_wage * hours
if day == "sunday":
    print("wages before:", daily_wages)
    daily_wages * 2
    print("wages after doubling:", daily_wages)

print(f"Daily wages: {daily_wages} euros")

# there are no errors so we assume that the problem is therefore with the block. 
# the following will return a boolean value of false for the condition

# ...

daily_wages = hourly_wage * hours
print("condition:", day == "sunday")
if day == "sunday":
    print("wages before:", daily_wages)
    daily_wages * 2
    print("wages after doubling:", daily_wages)

print(f"Daily wages: {daily_wages} euros")

# the issue is thus within the condition of the if statement.
# Notice how the "sunday" in the boolean expression was not capitalised, but the input was.
# fixing this can look as follows:

daily_wages = hourly_wage * hours
print("condition:", day == "Sunday")
if day == "Sunday":
    print("wages before:", daily_wages)
    daily_wages * 2
    print("wages after doubling:", daily_wages)

print(f"Daily wages: {daily_wages} euros")

# furthermore daily_wages * 2 does indeed double the value but it does not store the value
# daily_wages *= will store the value elsewhere
# this concludes the introduction to debugging

# Programming exercise: Fix the syntax
# The following program contains several syntactic errors. 
# Please fix the program so that the syntax is in order and the program works as specified

# Fix the program

number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")
print(f"{number} must be my lucky number!")
print("Have a nice day!")

# alternatively

number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number = number - 100
    print("Now its value has decreased by one hundred")
    print("Its value is now"+ str(number))
print(str(number) + " must be my lucky number!")
print("Have a nice day!")

# Programming exercise: Number of characters
# The function len can be used to find out the length of a string, among other things. 
# The function returns the number of characters in a string.

# Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

word = input("Please type in a word: ")
if len(word) > 1:
    print(f"There are {len(word)} letters in the word {word}")

print("Thank you!")

# Programming exercise: Typecasting
# When programming in Python, often we need to change the data type of a value. 
# For example, a floating point number can be converted into an integer with the function int:

# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. 
# Use the Python int function.
# You can assume the number given by the user is always greater than zero.

user_float = float((input("Please type in a number: ")))
int_split = int(user_float)
decimal_split = user_float - int_split

print(f"Integer part: {int_split}")
print(f"Decimal part: {decimal_split}")