#variable

#creating variable
var1 = "Hyperium "
var2 = "Op"
var3 = 37
var4 = 6.7

#printing variable type
print(type(var1))
print(type(var3))
print(type(var4))

#adding variable
print(var1 + var2)
print(var3 + var4)

#typecasting
a = "34"
b = "411"
print(int(a) + int(b))

"""
int()
float()
str()
"""

#we can print text any many times we want without typing it again and again
print(3* "repeat\n")

#input functiom
print("Enter your number")
number = input()
print("you entered " + number)

#assignment operators
a = 34
a += 12 # += will add 12 in 34
print(a)

# comparison operator
h = (13>=34)
print(h) # if 13 is greater than 34 or equal then it will print true else false

#my simple calculator for addition
print("enter your first number")
first = input()

print("enter your second number")
second = input()
print(int(first) + int(second))
