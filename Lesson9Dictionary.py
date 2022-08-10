"""
Created Tuesday Aug 9 2022

@author: doverto1
"""

# Dictionaries are unordered set of <key: value> pairs, where the keys are of immutable type,
# and must be unique within one dictionary. Dictionaries are index by keys.
# Referred to as "associate memories" or "associative arrays" in other languages.

# This creates an empty dictionary
grades = {}
print (len(grades))
print ()

# this creates a dictionary directly using comma-separated key: value pairs
grades = {
    'jack':90,
    'jill':100,
    'joe':99,
    'nat':95,
    'eric':100,
    'aubry':90
}
print (grades)
print ()

# this creates a dictionary with the constructor using sequences of key:value pairs
grades = dict([
    ('jack', 90), 
    ('jill', 100),
    ('joe', 99),
    ('nat', 95),
    ('eric', 100),
    ('aubry', 90)
])
print (grades)
print ()

# this creates a dictionary with the constructor using keyword arguments (can only be done if keys are simple strings)
grades = dict(jack=90, jill=10,  joe=90, nat=95, eric=100, aubry=90)
print (grades)
print ()

# this returns list of all keys used in dictionary in arbitrary order
print (grades.keys())
print ()

# this returns list of all keys used in dictionary in sorted order
print (sorted(grades.keys()))
print ()

# you can provide the key to extract the corresponding value
print (grades['nat'])
print ()

# you can modify the value associated with a key
grades['aubry'] = 93
print (grades)
print ()

# you can delete a key:value par from the dictionary
del grades['jack']
print (grades)
print ()

# you can check whether a key is in the dictionary
print ('hina' in grades)
print ()

# test
imdbRating = dict (interstellar=8.7, unbroken=7.2, divergent=6.8, wild=7.2, neighbors=6.4)
print (imdbRating) # True

print (imdbRating['interstellar']) # True

imdbRating['unbroken']=10
print (imdbRating) # True

# print (imdbRating['everest']) # False

print ()