# an exploration into loops with conditions

# Learning Objectives
# You will know how to create a while loop with a condition
# You will know what roles initialisation, formulating a condition and updating variables perform in a loop
# You will be able to create loops with different kinds of conditions

# example of while (true) loop:
# Print numbers until the variable a equals 5

a = 1
while True:
    print(a)
    a += 1
    if a == 5:
        break

# example where condition number < 10 is the requirement for the loop's block:

number = int(input("Please type in a number: "))

while number < 10:
    print(number)
    number += 1

print("Execution finished.")

# creating a loop involves 3 steps:

# initialisation - ask for user input, often called iteration or iterator variables. this is performed before the loop is first entered.
# condition - this defines how long the loop is to be executed and is set out at the beginning of the loop.
# updating iteration variables - the conditions are updated with each repetition of the loop (number += 1 for example).

# without any of these three components, the loop will likely not function correctly.
# a typical error is omitting the update step:

number = 1

while number < 10:
    print(number)

print("Execution finished.")

# (repeats 1 an infinite amount of times)

# Programming exercise: Print numbers
# Please write a program which prints out all the even numbers between two and thirty, using a loop. 
# Print each number on a separate line.

number = 1
while number <= 30:
    if number % 2 == 0:
        print(number)
    number += 1

# suggested solution is as follows:

number = 2
while number <= 30:
    print(number)
    number += 2

# Programming exercise: Fix the code: Countdown
# The program below has some syntactic issues. Fix it.
# This exercise is similar to the countdown exercise in the last section, but please don't use a while True loop this time round!

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number -= 1
print("Now!")

# Programming exercise: Numbers
# Please write a program which asks the user for a number. 
# The program then prints out all integer numbers greater than zero but smaller than the input.
# Please don't use the value True as the condition of your while loop in this exercise!

counting = 1
number = int(input("Upper limit: "))
while number > 0 and counting < number:
    print(counting)
    counting += 1

# suggested solution:

limit = int(input("Upper limit: "))
number = 1
while number < limit:
    print(number)
    number += 1

# sometimes hard coding the input is the easier way to write these solutions before changing the hard coding into user given input.
# visualisation tool on the python tutor website is also very handy.

# Programming exercise: Powers of two
# Please write a program which asks the user to type in an upper limit. 
# The program then prints out numbers so that each subsequent number is the previous one doubled, 
# starting from the number 1. That is, the program prints out powers of two in order.
# The execution of the program finishes when the next number to be printed would be greater 
# than the limit set by the user. No numbers greater than the limit should be printed.

upper_limit = int(input("Upper limit: "))
number = 1
while number <= upper_limit:
    print(number)
    number *= 2

# Programming exercise: Powers of base n
# Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).

upper_limit = int(input("Upper limit: "))
multi_by = int(input("Base: "))
number = 1
while number <= upper_limit:
    print(number)
    number = number * multi_by # or number *= multi_by

# Programming exercise: The sum of consecutive numbers, version 1

# Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers 
# (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows:

limit = int(input("Limit: "))
sum = 0
number = 0
while sum < limit:
    sum += number
    number += 1

print(sum)

# Building strings

# In the very first week of the course we learnt that it is possible to "build" 
# strings out of shorter strings with the + operator. For example, this is valid Python code:

words = "pride"
words = words + ", prejudice"
words = words + " and python"

print(words)

# or

words = "pride"
words += ", prejudice"
words += " and python"

print(words)

# Sample: pride, prejudice and python

# This also applies to f-strings, which may come in handy if values stored in variables 
# are needed as parts of the resulting string. For example this would work:

course = "Introduction to Programming"
grade = 4

verdict = "You have received "
verdict += f"the grade {grade} "
verdict += f"from the course {course}"

print(verdict)

# Sample: You have received the grade 4 from the course Introduction to Programming

# Programming exercise:
# The sum of consecutive numbers, version 2
# Please write a new version of the program in the previous exercise. 
# In addition to the result it should also print out the calculation performed.

limit = int(input("Limit: "))
sum = 1
total = 1
output = f"The consecutive sum: {sum}"
while total < limit:
    sum += 1
    output += f" + {sum}"
    total += sum

output += f" = {total}"
print(output)

# recommended solution:

limit = int(input("Limit: "))
number = 1
sum = 1
numbers = "1"
while sum < limit:
    number += 1
    sum += number
    # note that f-string can also be used like this
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {sum}")
