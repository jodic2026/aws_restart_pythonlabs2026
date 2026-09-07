# A loop is a segment of code that repeats. You will be introduced to two types of loops: the while loop and the for loop.

# Exercise 1: Working with a while loop
# A while loop makes a section of code repeat until a certain condition is met. In this exercise, you will create a Python script that asks the user to correctly guess a number.
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Importing random and writing a while loop
# You will use the import command to include code that someone else wrote. Up to now, you have been using built-in functions. Recall that a function is a piece of reusable code.
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


# Writing pseudocode
# Before you run the Python script, write out the logic of the while loop in written (non-code) sentences. This technique is called pseudocoding.

# Informing the user about the script
# In this activity, you will start a new Python script by creating the initial output that informs the user about what the script will do.
# Choose File > Save As... and save it as for-loop.py.
# To inform the user about your script, use the print() function:
print("Count to 10!")

# Writing the for loop
# In Python, you can include a large amount of functionality in a few words. This feature makes Python relatively easy to write compared to other programming languages, but it can also make Python code more difficult to read. In this activity, you will use the for statement, but you will also spend some time analyzing it after you see it run.
for x in range (0, 11):
    print(x)