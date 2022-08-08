"""
Created on Sunday August 7th

@author doverto1

"""

print()

# lists are mutable sequences, typically used to store collections of homogeneous items
# lists are represented by comma-separated items within square brackets

# here ares some lists
listPeople = ["tom", "harry", "jane", "liz"] 
listFlowers = ["rose", "lily", "tulip", "lantana"]
listPets = ["cat", "turtle", "goat", "dog"]
listNumFriends = [21, 33, 10, 51]

# list of heterogenous items tare not incorrect, just atypical
listAtypical = [1, 'cat', 0x45, 567]

# print lists
print ("listPeople      ", listPeople)
print ("listFlowers     ", listFlowers)
print ("listPets        ", listPets)
print ("listNumFriends  ", listNumFriends)
print ("listAtypical    ", listAtypical)

print ()

# just like strings, you can do following with lists:

# concatenate lists
listConcat = listPeople + listPets
print ("listConcat      ->", listConcat)

# length of list
print ("len(listPeople) ->", len(listPeople))

# refer to item in list with index
print ("listPeople[2]   ->", listPeople[2])
print ("listPeople[-3]  ->", listPeople[-3])

# slice list with [startIndex:endIndex]
print ("listPeople[2:]  ->", listPeople[2:])

print()

# unlike strings, lists are mutable

# assign to an index
listPets[0] = 'trex'
print(listPets)

# assign to a slice
listPets[0:2] = ['python', 'elephant']
print(listPets)

# delete a slice
listPets[2:4] = []
print(listPets)

# append new items to a list
listPets.append('fox')
print(listPets)

# clear a list by assigning to an empty list
listPets[:] = []
print(listPets)

print()


# we can create lists from other lists

# we can assign lists to other lists
sublistPeople = listPeople[0:3]
print("listPeople   ", listPeople)
print("sublistPeople    ", sublistPeople)

print()

# we can create lists from other list items
listCompiled = [(listPeople[0].upper(), listFlowers[0], listNumFriends[0]+10)]
print ("listPeople:     ", listPeople)
print ("listFlowers:    ", listFlowers)
print ("listNumFriends: ", listNumFriends)
print ("listCompiled    ", listCompiled)

# we can also nest lists
listNested = [listPeople, listFlowers]
print ("listPeople:     ", listPeople)
print ("listFlowers:    ", listFlowers)
print ("listNested      ", listNested)

# nested list at index 0 - so essentially listPeople
print ("listNested[0]:  ", listNested[0])

# nested lsit at index 1 - so essentially listFlowers
print ("listNested    ", listNested[1])

# pick item at index 1 of nested list at index 0
print ("listNested[0][1]:    ", listNested[0][1])

# pick item at index 2 of nested list at index 1
print ("listNested[1][2]:   ", listNested[1][2])

print()

# the Python standard library provides many different methods to manipulate lists
# https://docs.python.org/3/tutorial/datastructures.html
# below are ones that are most frequently used

list1 = [100, 200, 300]
list2 = [5, 15, 25]
list3 = [10, 50, 50, 20, 0, 10, 50]
print ("list1:  ", list1)
print ("list2:  ", list2)
print ("list3:  ", list3)

# Add an item to the end of the list. Equivalent to list1(len(list)):] = [-6000]
list1.append(-400)
print ("list1:  ", list1)

# Extend the list by appending all items in list1. Equivalent to list2(list2):] = list1
list2.extend(list1)
print ("list2:  ",list2)

# Insert and item at index [3]
list2.insert (3, -400)
print ("list2:  ", list2)

# Remove the first item from list2 whose value is -400
list2.remove(-400)
print ("list2:  ", list2)

# Remove the item at index [6]
del list2[6]
print ("list2:  ", list2)

# Remove and return the last item in the list
list2.pop()
print ("list2:  ", list2)

# Return the index in list3 of the first item whose value is 50
print (list3.index(50))

# Return the number of times 50 appears in list3
print (list3.count(50))

# Reverse the items of list3 in place.
list3.reverse()
print ("list3:  ", list3)

# Sort the items of list3 in place.
list3.sort()
print ("list3:  ", list3)

# Remove all items from the list
list3.clear()
print ("list3:  ", list3)

# Delete the list - so now any reference to the list will be an error
del list3
# print ("list3:  ", list3)

print()

# test

myStr = "CIS 415"
myList1 = ['CIS', '415']
myList2 = ['CIS', 'SCM', 'BDA']

print (myStr[1]) # true print I

print (myList1[1]) # true print '415'

print (myList2[-2]) # true print 'SCM'

# print (MyList1) # false 

# myStr[4] = '5' # false strings are immutable

myList2.append('MKTG') #true
print(myList2)

print()