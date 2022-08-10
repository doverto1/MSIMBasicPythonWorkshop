"""
Created Tuesday August 9 2022

@author doverto1
"""
# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations operations like union, intersection, difference, and symmetric difference.

# Duplicates will automatically be removed.
basket = ('apple', 'orange', 'pear', 'orange', 'banana')
print (basket)
print()

# test for membership
print ('orange' in basket)
print()

# another way to declare singe character sets
someChars = set ("235345#$$%^$%&abdfsdf")
print (someChars)
print()

# set operations
set1 = set('abracadabra')
set2 = set('alacazam')

print ("set1:       ", set1)
print ("set2:       ", set2)

# union
print ("set1 | set2:    ", set1 | set2)

# intersection
print ("set1 & set2:    ", set1 & set2)

# difference
print ("set1 - set2:    ", set1 - set2)

# symmetric difference
print ("set1 ^ set2:    ", set1 ^ set2)

print()

# test

set1 = set ('abracadabra')
set2 = set ('alacazam')
print   ((set1 ^ set2) - ((set1 | set2) - (set1 & set2))) # True (prints set())
print   ((set1 ^ set2) - ((set1 - set2) | (set1 - set2))) # True

set1 = {'dog', 'cat', 'deer'}
print (set1)

# set2 = set ('sparrow', 'hawk', 'eagle')
# print (set2) # False

set3 = set ('abc123')
print (set3) # True

set4 = set ('\'abc123\'')
print (set4) # True

print ()