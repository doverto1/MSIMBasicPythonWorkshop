"""
Created on Saturday August 6th

@author doverto1

"""

# print()

# #strings can be concatenated using +

# print ("left string > " + "< right string")

# lstr = "CIS"
# rstr = "415"
# lrstr = lstr + rstr
# print (lrstr)

# print()

# print ("repeat ..."*3)
# print()


# # strings can be counted from the left using +ve indices, starting with 0

# word = "Python"

# print (word[0])

# print (word[1])

# print (word[2])

# print (word[3])

# print (word[4])

# print (word[5])

# print()


# # strings can be counted from the right using -ve indices, starting -1
# print (word[-1])

# print (word[-2])

# print (word[-3])

# print (word[-4])

# print (word[-5])

# print (word[-6])

# print() 

# # strings can be sliced with [startIndex:endIndex]:
# # - startIndex is included and endIndex is excluded
# # - startIndex must be < endIndex, else empty string is returned
# # - if a slice index is out of range, python will go as far as it can

# print (word[0:2])

# print (word[2:6])

# print (word[2:10])

# print ( word[-3:-2])

# print ( word[-3:-6])

# print (word[-3:6])

# print()


# omitted startIndex is defaulted to 0, omitted endIndex is defaulted to strlen
# this ensures anyString[:n] + anyString[n:] = anyString

# print (word[:2])

# print (word[4:])

# print (word[-2:])

# print (word[:4] + word[4:])

# print()

# Python strings cannot be changed - they are immutable
# attempting to assign to an index position will result in an error
# word[0] = 'J'

# if you need a different string, you should just create a new one
# newword = 'J' + word[1:]

# print(newword)

# print()

# the Python standard library provides many different methods to manipulate strings
# https://docs.python.org/3/library/stdtypes.html#string-methods
# below are ones that are most frequently used

# length of string
# print(len('Python'))

# #check if substring is in string
# print ('th' in 'Python')

# # find index of substring in string
# print('Python'.find('th'))

# # check if string start with substring
# print ('Python'.startswith('Py'))

# # check if string ends with substring
# print ('Python'.endswith('Py'))

# # convert string to lowercase
# print ('PYTHON'.lower())

# # convert to uppercase
# print ('python'.upper())

# # remove trailing blanks
# print ('     python     '.strip())

# sprit string using specified character as delimiter
# print ('1, 2, 3, 4, 5'.split(', '))

# # join iterable elements with specified character as delimiter
# names = ['john','jane','sandra','mike','scott']
# sep = ','
# print(sep.join(names))

# #split string at line feeds and carriage returns
# print ('there \n are \n four \n lines'.splitlines())

# print()

#test

myWord = "CIS 415 Classroom"

# print (len(myWord)) #true

# print (myWord[0:7]) #true

# print (myWord[:6] + myWord[6:]) #true

# print (myWord[:100]) #true

# print (myWord[100:-5]) #true but does not print anything

# print (myWord[-9:100]) #true

# print (myWord[]) #false

# print()