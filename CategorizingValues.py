# With Python, you can mix types in a list. In this lab, you will create a list with different types and print the values.

# Exercise 1: Creating a mixed-type list
# You can mix data types in a Python list. In other languages, this capability is not a feature of lists. In this exercise, you will explore this capability.
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))