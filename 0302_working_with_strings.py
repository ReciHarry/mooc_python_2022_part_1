# on further exploration into string functionality and practise

# Learning Objectives
# You will be able to use the operators + and * with strings
# You will know how to find out the length of a string
# You will know what is meant by string indexing
# You will know how to look for substrings within a string

# Using string operations together with a loop we can write a program which draws a pyramid:

n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

# Sample output:

#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#   *****************
#  *******************

# Programming exercise: String multiplied
# Please write a program which asks the user for a string and an amount. 
# The program then prints out the string as many times as specified by the amount. 
# The printout should all be on one line, with no extra spaces or symbols added.

user_string = input("Please type in a string: ")
string_multiplier = int(input("Please type in an amount: "))
print(user_string * string_multiplier)

# The length and index of a string
# The function len returns the number of characters in a string, which is always an integer value. 
# For example, len("hey") returns 3, because there are three characters in the string hey.

# The following program asks the user for a string and then prints it "underlined". 
# The program prints a second line with as many - characters as is the length of the input:

input_string = input("Please type in a string: ")
print(input_string)
print("-"*len(input_string))

# Sample output: 

# Please type in a string: Hi there!

# Hi there!
# ---------

# Programming exercise: The longer string

# Please write a program which asks the user for two strings 
# and then prints out whichever is the longer of the two - that is, whichever has the more characters. 
# If the strings are of equal length, the program should print out "The strings are equally long".

string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")
if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string2) > len(string1):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")

# As strings are essentially sequences of characters, any single character in a string can also be retrieved. 
# The operator [] finds the character with the index specified within the brackets.
# The index refers to a position in the string, counting up from zero. 
# The first character in the string has index 0, the second character has index 1, and so forth.

# For example

input_string = input("Please type in a string: ")
print(input_string[0])
print(input_string[1])
print(input_string[3])

# Please type in a string: monkey
# m
# o
# k

# Since the first character in a string has the index 0, the last character has the index length - 1. 
# The following program prints out the first and the last characters of a string:

input_string = input("Please type in a string: ")
print("First character: " + input_string[0])
print("Last character: " + input_string[len(input_string) - 1])

# Please type in a string: testing
# First character: t
# Last character: g

# The following program loops through all the characters in a string from first to last:

input_string = input("Please type in a string: ")
index = 0
while index < len(input_string):
    print(input_string[index])
    index += 1

# Please type in a string: test
# t
# e
# s
# t

# You can also use negative indexing to access characters counting from the end of the string. 
# The last character in a string is at index -1, the second to last character is at index -2, and so forth. 
# You can think of input_string[-1] as shorthand for input_string[len(input_string) - 1].

input_string = input("Please type in a string: ")
print("First character: " + input_string[0])
print("Last character: " + input_string[-1])

# Please type in a string: testing
# First character: t
# Last character: g

# Programming exercise: End to beginning
# Please write a program which asks the user for a string. 
# The program then prints out the input string in reversed order, 
# from end to beginning. Each character should be on a separate line.

user_string = input("Please type in a string: ")
string_index = -1
while string_index >= -len(user_string):
    print(user_string[string_index])
    string_index = string_index -1
    # string_index -= 1 for shorthand

# Programming exercise: Second and second to last characters
# Please write a program which asks the user for a string. 
# The program then prints out a message based on whether the second character and the second to last character are the same or not.

user_string = input("Please type in a string: ")
if user_string[1] == user_string[-2]:
    print(f"The second and the second to last characters are {user_string[1]}")
else:
    print("The second and the second to last characters are different")

# Programming exercise: A line of hashes
# Please write a program which prints out a line of hash characters, the width of which is chosen by the user.

hash_width = int(input("Width: "))
hash = "#"
print(hash * hash_width)

# Programming exercise: A rectangle of hashes
# Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

hash_width = int(input("Width: "))
hash_height = int(input("Height: "))
hash = "#"
scaler = 0
while scaler < hash_height:
    print(hash * hash_width)
    scaler += 1

# Programming exercise: Underlining
# Please write a program which asks the user for strings using a loop. 
# The program prints out each string underlined as shown in the examples below. 
# The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

dash = "-"
while True:
    user_input = input("Please type in a string: ")
    print(user_input)
    print(dash * len(user_input))

    if user_input == "":
        break

# Better to do it this way:

while True:
    string = input("Please type in a string: ")
    if string == "":
        break
    print(string)
    print(len(string) * "-")

# Programming exercise: Right-aligned
# Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
# If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

string = input("Please type in a string: ")
hash = "*"
hash_count = 20 - len(string)
print((hash_count * hash) + string)

# alternatively:

word = input("Please type in a string: ")
 
aligned = (20 - len(word)) * "*" + word
 
print(aligned)

# Programming exercise: A framed word
# Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. 
# The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

word = input("Word: ")
hash = "*"
centre = word.center(28)

print(30 * hash)
print(hash + centre + hash)
print(30 * hash)

# alternatively

word = input("Word: ")
 
print("*" * 30)
spaces_at_start = (28 - len(word)) // 2
spaces_at_end = spaces_at_start
 
# If the word length is odd, one is added to the spaces at the end of the word
# to get all 30 characters filled
if len(word) % 2 != 0:
    spaces_at_end += 1
 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30)

# Substrings and slices

input_string = "presumptious"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])

# pre
# umptio
# pre
# umptious

# Programming exercise: Substrings, part 1
# Please write a program which asks the user to type in a string. 
# The program then prints out all the substrings which begin with the first character, from the shortest to the longest. 

word = input("Please type in a string: ")
index = 1
while index <= len(word):
    print(word[0:index])
    index += 1

# Programming exercise: Substrings, part 2

# Please write a program which asks the user to type in a string. 
# The program then prints out all the substrings which end with the last character, 
# from the shortest to the longest.

word = input("Please type in a string: ")
index = -1
while index >= -len(word):
    print(word[index:])
    index -= 1

# Searching for substrings
# The in operator can tell us if a string contains a particular substring. 
# The Boolean expression a in b is true, if b contains the substring a.

input_string = "test"

print("t" in input_string)
print("x" in input_string)
print("es" in input_string)
print("ets" in input_string)

# True
# False
# True
# False

# Search functionality: 

input_string = "perpendicular"

while True:
    substring = input("What are you looking for? ")
    if substring in input_string:
        print("Found it")
    else:
        print("Not found")

    break # just so I don't get pylance error

# What are you looking for? perp
# Found it
# What are you looking for? abc
# Not found
# What are you looking for? pen
# Found it

# Programming exercise: Does it contain vowels
# Please write a program which asks the user to input a string. 
# The program then prints out different messages if the string contains any of the vowels a, e or o.
# You may assume the input will be in lowercase entirely. 

input_string = input("Please type in a string: ")

if "a" in input_string:
    print("a found")
else:
    print("a not found")

if "e" in input_string:
    print("e found")
else:
    print("e not found")

if "o" in input_string:
    print("o found")
else:
    print("o not found")

# alternatively, more clean version:

string = input("Please type in a string: ")
vowels = "aeo"
index = 0
 
while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1

# infact, much better version. yoink.

# The operator in returns a Boolean value, so it will only tell us if a substring exists in a string, 
# but it will not be useful in finding out where exactly it is. Instead, the Python string method find can be used for this purpose. 
# It takes the substring searched for as an argument, and returns either the first index where it is found, 
# or -1 if the substring is not found within the string.

input_string = "test"

print(input_string.find("t"))
print(input_string.find("x"))
print(input_string.find("es"))
print(input_string.find("ets"))

# 0
# -1
# 1
# -1

input_string = "perpendicular"

while True:
    substring = input("What are you looking for? ")
    index = input_string.find(substring)
    if index >= 0:
        print(f"Found it at the index {index}")
    else:
        print("Not found")

        break # just to clear up any errors

# What are you looking for? perp
# Found it at the index 0
# What are you looking for? abc
# Not found
# What are you looking for? pen
# Found it at the index 3

# Methods
# Above we used the string method find. Methods work quite similarly to the functions covered in the previous part. 
# What distinguishes them from functions is that methods are always attached to the object they are called on. 
# The object is the entity named before the method in the method call. 
# In the case of find the object is the string where the method looks for the substring it has as an argument.

# Programming exercise: Find the first substring
# Please write a program which asks the user to type in a string and a single character. 
# The program then prints the first three character slice which begins with the character specified by the user. 
# You may assume the input string is at least three characters long. 
# The program must print out three characters, or else nothing.

word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)
if index >= 0 and index < (len(word) - 3):
    print(word[index:(index+3)])

# Programming exercise: Find all the substrings
# Please make an extended version of the previous program, 
# which prints out all the substrings which are at least three characters long, 
# and which begin with the character specified by the user. 
# You may assume the input string is at least three characters long.

word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1

# Programming exercise: The second occurrence
# Please write a program which finds the second occurrence of a substring. 
# If there is no second (or first) occurrence, the program should print out a message accordingly.
# In this exercise the occurrences cannot overlap. 
# For example, in the string aaaa the second occurrence of the substring aa is at index 2.

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index1 = string.find(substring)
i = -1

if index1 != -1:
    i = string.find(substring, index1 + len(substring))

if i == -1:
    print('The substring does not occur twice in the string.')
else:
    print(f"The second occurrence of the substring is at index {i}.")