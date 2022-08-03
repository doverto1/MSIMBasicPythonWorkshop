"""
Created on Tuesday August 2nd 15:53
@author: doverto1
"""
import math

print("Power Operator: **")

print("2**4 = ", 2**4)

print("-3**2 = ", -3**2)
print("-(3**2) = ", -(3**2))

print("3**-2 = ", 3**-2)

print()

print("Unary and bitwise operators: -  ~")

print("-2 = ", -2)

print("~2 = ", ~2, "(bitwise inversion)")

print("Floor Operator: 101//2 =", 101//2)

print("Modulus Operator: 101%2 =", 101%2)

print()

print("Shifting operators: >> <<")

print("100 >> 3 = ", 100 >> 3)

print("  same as : 100 // (2**3) = ", 100 // (2**3))

print("100 << 3 = ", 100 << 3)

print()

print( "Binary bitwise operators: | & ^")

print("3 | 0 = ", 3 | 0)

print("3 ^ 3 = ", 3 ^ 3)

print("3 & 0 = ", 3 & 0)

print()

print("Comparisons: > >= < <= == in not in")

print("5 > 2?", 5 > 2) #True

print("5 == 3?", 5 == 3) #False

print ("5 <= 4?", 5 <= 4) #True

print("2 in (1, 2, 3)", 2 in (1, 2, 3)) #True

print ("5 not in (1, 2, 3)?", 5 not in (1, 2, 3)) #True

print ()

print("Boolean operations: AND OR NOT")

print("5 > 2 AND 5 == 2?", (5 > 2) and (5 == 2)) #False

print("5 > 2 OR 5 == 2?", (5 > 2) or (5 == 2)) #True

print ("5 NOT == 2?", not (5 == 2)) #True

#Multiple assignment
a = 0
b = 1
print(a, b)

c, d = 0,1
print(c,d)

#advanced assignment
a, b = 0, 1

a, b = b, a+b #a is assigned the value of b and b becomes a+b
print(a, b) # 1, 1

#use the math module


var1 = 2
var2 = 3

#round to the nearest integer
print (round(var1/var2)) #1

#floor(x): the largest integer less than or equal to x
print(math.floor(var1/var2)) # 0

#ceil(x): the smallest integer greater than or equal to x
print(math.ceil(var1/var2)) # 1

#pow (x, y): x raised to the power y
print(pow(var1,var2)) # 8

# abs (x): absolute value of x
print(abs(var1 - var2))   #1

print(math.sqrt(var1)) # 1.4142135623730951


print()
#test

var1 = 5
var2 = 2
var3 = 2

var4 = math.sqrt(pow(var1,var2)) #yes 5.0

var5 = pow(var1-var2,var3) #yes 9

print(var4, var5) #yes

print()