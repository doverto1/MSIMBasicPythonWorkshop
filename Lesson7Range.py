"""

Created Monday August 08 2022
author: @doverto1

"""
# The for statement in Python differs a bit from what you may be used to.
# Rather than always iterating over an arithmetic progression of numbers, or
# giving you the ability to define both the iteration step and halting
# condition, Python's for statement iterates ove the items of an iterable
# sequence (such as a list, tuple, or string), in the order that they appear
# in the sequence.

words = ['cat', 'dog', 'cow', 'parrot', 'hamster', 'goat']
for word in words:
    print (word, len(word))

print ()

# The range function generates arithmetic progressions

# range(n) -> 0,....,n-1 in increments of 1
for i in range(5):
    print (i, end=",")
print ()

# range (m,n) ->m,.....,n-1 increments of 1
# if m >= n, returns nothing
for i in range(3,10):
    print (i, end=",")
print ()

# counts in positive increments if n > m, and k is positive
# range(m, n, k) ->m, .....,<=n-1 in increments of k
for i in range(3, 10,2):
    print (i, end=',')
print()

# counts in negative increments if n < m, and k is negative
# range (m, n, k) -> m, ...., >=n+1 in increments of k
for i in range(10, -30, -5):
    print (i, end=',')
print ()

words = ['jane', 'john', 'mark', 'harry', 'mike', 'ed']
wordlist = []
for i in range( len(words)):
    wordlist.append([i, words[i]])
print (wordlist)

print()

# Note: The object returned by range() behaves as if it is a list,
# but in fact it isn't. It is an object which returns the successive items of
# the desired sequence when you iterate over it, but it doesn't really make
# the list, thus saving space

r = range(0, 20, 2)
print (r)
print (list(r))
print (11 in r)
print (r.index(10))
print (r[5])
print (r[:5])
print (r[-1])

print ()


# Testing range object for equality with == and != compares them as sequences.
# That is, two range object are considered equal if they represent the same sequence of values
print (range(0) == range(2, 1, 3))

print ()

# test

# for i in range():
#     print (i, end=',')
# print ()  # false

for i in range(10):
    print (i, end=',')
print () # True

for i in range(0,-10):
    print (i, end=',')
print () # True

for i in range(0,-10,-2):
    print (i, end=',')
print () # False
