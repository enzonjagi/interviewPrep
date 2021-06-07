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
