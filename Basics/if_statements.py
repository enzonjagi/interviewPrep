"""temp = 25
if temp > 30:
    print("Hot day ey!")
elif temp > 20:
    print("Not bad, but bring sunscreen")

else: 
    print("No sunscreen")
"""

#Assignment
"""
Code asks for weight,
 then asks if it's in KG(k or K) of Lbs(l or L)
 it then converts to the other

Solution
    Ask for input(weight and metric) and store in variables
    then check for (l/L) or (k/K): if statements and logical operators
    use the conversion metric(1kg = 2.205lbs) to give output required
"""
weightValue = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")

convert = 2.205

if unit == "l" or unit == "L":
    print(weightValue/convert)
elif unit=="k" or unit=="K":
    print(weightValue*convert)
else:
    print("Invalid metric")
