# A few exercises with regard to a further look into variables.

# Learning Objectives
# You will be able to use variables in different contexts
# You will know what kind of data can be stored in variables
# You will understand the difference between strings, integers and floating point numbers

# str(result) is essentially parseInt(String s)
# print("The result is", result) would work in the case of string interacting with integer ("" + result) would not work however.

# f-strings are considered the most simple use of formatting printouts.
# print(f"The result is {result}")
# f after paranthesis indicates f-string to python. Curly brackets notifies variable presence and the string essentially absorbs the value.
# as another example print(f"Hi {name}, you are {age} years old. You live in {city}.") 
# This saves a lot of time with regard to screwing around with opening and closing the speech marks.
# Python 3.6+ required for f-strings.

# Programming exercise: Extra space
# Please fix the code so that the printout looks right. 
# Notice especially how the comma notation in the print command automatically inserts a space around the different comma-separated parts.


name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

# floating point numbers (floats)

# Programming exercise: Arithmetics

x = 27
y = 15

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

# Programming exercise: Fix the code: Print a single line
# Each print command usually prints out a line of its own, complete with a change of line at the end. 
# However, if the print command is given an additional argument end = "", it will not print a line change.

print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)