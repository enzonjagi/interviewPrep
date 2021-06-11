numbers = [1,2,3,4,5]
print(numbers)
reverse = []

#reverse numbers
"""
    Use for/while loop to check if the two lists are equal in length
    assign the last value of numbers to a variable(lastValue)
    (have a check to see if lastValue == numbers[0]: break)
    else:append the last value to reverse and then subtract -1 to the lastValue
"""
for i in numbers:
    reverse.append(i)
print(reverse)

