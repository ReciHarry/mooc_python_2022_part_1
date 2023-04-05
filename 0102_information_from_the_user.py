# This section will cover the very basic user input exercises

# Learning Objectives
# You will know how to write a program which uses input from the user
# You will know how to use variables to store input and print it out
# You will be able to combine strings

# Programming exercise: Name Twice
# Please write a program which asks for the user's name and then prints it twice, on two consecutive lines.

name = input("What is your name?")
print(name)
print(name)

# Programming exercise: Name and exclamation marks
# Please write a program which asks for the user's name and then prints it 
# out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# another between the two names and a third one at the end of the line.

name2 = input("What is your name?")
print("!" + name2 + "!" + name2 + "!")

# Programming exercise: Name and address
# Please write a program which asks for the user's name and address. 

first_name = input("Given name:")
family_name = input("Family name:")
street_address = input("Street address:")
city_code = input("City and postal code:")

print(first_name + " " + family_name)
print(street_address)
print(city_code)

# Programming exercise: Fix the code: Utterances
# Here is a program which should ask for three utterances and print them out.

part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")

# Programming exercise: Story
# Please write a program which prints out the following story. 
# The user gives a name and a year, which should be inserted into the printout.

story_name = input("Please type in a name:")
story_year = input("Please type in a year:")
print(story_name + " is a valiant knight, born in the year " + story_year + ". One morning " 
      + story_name + " woke up to an awful racket: a dragon was approaching the village. Only " 
      + story_name + " could save the village's residents.")