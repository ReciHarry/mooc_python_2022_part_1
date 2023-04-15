# a small introduction to simple loops

# Learning Objectives
# You will know what a loop means in programming
# You will be able to use a while True loop in your programs
# You will know how to use the break command to break out of a loop

# Let's have a look at a program which asks the user to type in a number and then prints out the number squared. This continues until the user types in -1.

while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break

    print(number ** 2)

print("Thanks and bye!")

while True:
    code = input("Please type in your PIN: ")
    if code == "1234":
        break
    print("Incorrect...try again")

print("Correct PIN entered!")

# Programming exercise: Shall we continue?
# Let's create a program along the lines of the example above. 
# This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". 
# Then the program should print out "okay then" and finish. Please have a look at the example below.

while True:
    print("hi")
    u_continue = input("Shall we continue? ")

    if u_continue == "no":
        print("okay then")
        break

# Programming exercise: Input validation
# Please write a program which asks the user for integer numbers.
# If the number is below zero, the program should print out the message "Invalid number".
# If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
# In either case, the program should then ask for another number.
# If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

from math import sqrt

while True:
    user_number = int(input("Please type in a number: "))

    if user_number < 0:
        print("Invalid number")
    elif user_number > 0:
        print(sqrt(user_number))
    else:
        print("Exiting...")
        break

# Programming exercise: Fix the code: Countdown
# This program should print out a countdown. The code is as follows:

number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  
  if number == 0:
    break

print("Now!")

# Programming exercise: Repeat password
# Please write a program which asks the user for a password. 
# The program should then ask the user to type in the password again. 
# If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

password_original = input("Password: ")

while True:
    password_check = input("Repeat password: ")

    if password_check != password_original:
        print("They do not match!")
    else:
        print("User account created!")
        break

# An example of a realistic failsafe mechanism on a PIN number:

attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    # this is printed if the code was incorrect AND there have been less than three attempts
    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")

# Programming exercise: PIN and number of attempts
# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. 
# The program should then print out the number of times the user tried different codes.
# If the user gets it right on the first try, the program should print out something a bit different

attempts = 0
pin = 4321

while True:
    pin_check = int(input("PIN: "))

    if pin_check != pin:
        print("Wrong")
        attempts += 1

    else:
        if attempts == 0:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts + 1} attempts")
        break

# Programming exercise: The next leap year
# Please write a program which asks the user for a year, and prints out the next leap year.

user_year = int(input("Year: "))
is_it_leap = 0

while (user_year + is_it_leap) % 4 != 0:
    is_it_leap += 1
    
if (user_year + 4) % 100 == 0:
    if (user_year + 4) % 400 != 0:
        print(f"The next leap year after {user_year} is {user_year + 8}")
elif user_year % 4 == 0:
    print(f"The next leap year after {user_year} is {user_year + 4}")
elif (user_year + is_it_leap) % 100 == 0 and (user_year + is_it_leap) % 400 != 0:
        print(f"The next leap year after {user_year} is {user_year + is_it_leap + 4}")
else:
    print(f"The next leap year after {user_year} is {user_year + is_it_leap}")

# meanwhile when you actually know what you're doing:
# what a trainwreck

start_year = int(input("Year: "))
year = start_year + 1
while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
 
    year += 1
 
print(f"The next leap year after {start_year} is {year}")

# so the idea is to turn a number into another number rather than combine 2 numbers together for a more streamlined approach.


# Programming exercise: Story
# Please write a program which keeps asking the user for words. 
# If the user types in end, the program should print out the story the words formed, and finish.

story = ""
last_word = ""

while True:
    user_word = input("Please type in a word: ")
    if user_word == "end" or user_word == last_word:
        break

    story += user_word + " "
    last_word = user_word

print(story)

# Programming exercise: Working with numbers
# Please write a program which asks the user for integer numbers. 
# The program should keep asking for numbers until the user types in zero.

# After reading in the numbers the program should print out how many numbers were typed in. 
# The zero at the end should not be included in the count.

# The program should also print out the sum of all the numbers typed in. 
# The zero at the end should not be included in the calculation.

# The program should also print out the mean of the numbers. 
# The zero at the end should not be included in the calculation. 
# You may assume the user will always type in at least one valid non-zero number.

# The program should also print out statistics on how many of the numbers were positive and how many were negative. 
# The zero at the end should not be included in the calculation.

print("Please type in integer numbers. Type in 0 to finish.")
number_count = 0
numbers_sum = 0
numbers_pos = 0
numbers_neg = 0

while True:
    integers = int(input("Number: "))

    if integers == 0:
        break

    number_count += 1
    numbers_sum = numbers_sum + integers

    if integers > 0:
        numbers_pos += 1
    else:
        numbers_neg += 1

print(f"Numbers typed in {number_count}")
print(f"The sum of the numbers is {numbers_sum}")
print(f"The mean of the numbers is {float(numbers_sum / number_count)}")
print(f"Positive numbers {numbers_pos}")
print(f"Negative numbers {numbers_neg}")