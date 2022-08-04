"""
Donald Overton
"""
import math
#Exercise 1
# euros = 200
# xchng = 1.02

# dollars = round ( euros*xchng, 2)

# print("Euros = ", euros)
# print("Exchange Rate = ", xchng)
# print("Dollars = ", dollars)

#Exercise 2
# billedAmount = 123.45
# tipPercentage = 0.20
# tip = round(billedAmount*tipPercentage,2)

# # totalDue = round(billedAmount*(1+tipPercentage),2)
# totalDue = round(billedAmount+tip,2)
# print("Billed Amount = ", billedAmount)
# print("Tip Percentage = ", tipPercentage)
# print("Tip = ", tip)
# print("Total Due = ", totalDue)

#Exercise 3
# radius = 10
# circumference = round(2*math.pi*radius,2)
# area = math.pi*pow(radius,2)
# area = round(area, 2)

# print("Radius = ", radius)
# print("Circumference = ", circumference)
# print("area = ", area)

#Exercise 4
# number = 22
# remainder = number%2
# isEven = (remainder==0)

# print("Number = ", number)
# print("Number%2 = ", remainder)
# print("Is number even?", isEven)

#Exercise 5
dollars = 259
dollarsLeftToBreak = dollars

num20s = math.floor(dollarsLeftToBreak/20)
dollarsLeftToBreak = dollarsLeftToBreak%20

num10s = math.floor(dollarsLeftToBreak/10)
dollarsLeftToBreak = dollarsLeftToBreak%10

num5s = math.floor(dollarsLeftToBreak/5)
dollarsLeftToBreak = dollarsLeftToBreak%5

num1s = math.floor(dollarsLeftToBreak/1)

print("Dollar Amount = ", dollars)
print("Number of 20s = ", num20s)
print("Number of 10s = ", num10s)
print("Number of 5s = ", num5s)
print("Number of 1s = ", num1s)