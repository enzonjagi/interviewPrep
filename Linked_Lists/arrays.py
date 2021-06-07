#operations
"""
Importing
    import array | import array as arr | from array import *
"""
import array

#Creating array syntax
#variable = array.array(type_code, [array, items])
a = array.array('i', [1,2,3,4,5,6])
print(a)

#Accessing Arrays
#use index ordering to access items
#for example
print(a[-3]) #Should print the third-last item(4)

#Array operations
#length
print(len(a))
#adding: 
# append(add 1 item), extend(add more than one), insert(add to specific position)
a.append(7)
a.insert(0, 0)
a.extend([8,9,10])
print(a)
