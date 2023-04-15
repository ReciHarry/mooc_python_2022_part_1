# a more elaborate look at conditional statements

# Learning Objectives
# You will know how to create multiple branches within conditional statements
# You will understand the purpose of if, elif and else statements within a conditional statement
# You will be able to use the modulo operation % in Boolean expressions

# Programming exercise: Age of maturity
# Please write a program which asks the user for their age. 
# The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.

user_age = int(input("How old are you? "))

if user_age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")

# Adding the else statement allows us to create a secondary 'if' in a sense.
# Likewise, we can use an elif statement (else if) which factors in more outcomes - there is no limit on how many can be used

goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("The home team won!")
elif goals_away > goals_home:
    print("The away team won!")
else:
    print("It's a tie!")

# In the same respect, an else statement is not needed to close, for example:

print("Holiday calendar")
date = input("What is the date today? ")

if date == "Dec 26":
    print("It's Boxing Day")
elif date == "Dec 31":
    print("It's Hogmanay")
elif date == "Jan 1":
    print("It's New Year's Day")

print("Thanks and bye.")

# Programming exercise: Greater than or equal to
# Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater. 
# If the numbers are equal, the program should print a different message.

first_int = int(input("Please type in the first number: "))
second_int = int(input("Please type in another numbers: "))

if first_int > second_int:
    print(f"The greater number was: {first_int}")
elif second_int > first_int:
    print(f"The greater numbe was: {second_int}")
else:
    print("The numbers are equal!")

# Programming exercise: The elder
# Please write a program which asks for the names and ages of two persons. 
# The program should then print out the name of the elder.

print("Person 1:")
user_name1 = input("Name: ")
user_age1 = int(input("Age: "))
print("Person 2:")
user_name2 = input("Name: ")
user_age2 = int(input("Age: "))

if user_age1 > user_age2:
    print(f"The elder is {user_name1}")
elif user_age2 > user_age1:
    print(f"The elder is {user_name2}")
else:
    print(f"{user_name1} and {user_name2} are the same age")

# Programming exercise: Alphabetically last
# Python comparison operators can also be used on strings. String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if

# the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
# only the standard English alphabet of a to z, or A to Z, is used.

# Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

# You can assume all words will be typed in lowercase entirely.

first_word = input("Please type in the 1st word: ")
second_word = input("Please type in the 2nd word: ")

if first_word > second_word:
    print(f"{first_word} comes alphabetically last.")
elif second_word > first_word:
    print(f"{second_word} comes alphabetically last.")
else:
    print("You gave the same word twice.")