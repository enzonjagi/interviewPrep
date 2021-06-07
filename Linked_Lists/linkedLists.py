#List Basics
"""
    Swap the first and last values of the list given,
    
    Solution:
        Assign the values to independent variables,
        then swap positions on the list
"""

l = ["banana", "apple", "microsoft"]
print(l)
first = l[0]
last = l[-1]

l[0] = last
l[-1] = first
print(l)

"""
Another Solution
    Assign the first value to a variable
    then refer the list position to the last value
    then refer the last postion to the variable
    See Below

"""
temp = l[0]
l[0] = l[-1]
l[-1] = temp
print(l)

#Linked List Practice
