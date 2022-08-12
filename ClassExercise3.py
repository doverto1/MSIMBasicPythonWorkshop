"""
Created Wednesday Aug 10

@author: doverto1
"""
import math
for i in range (5):
    print ("hello")
    
for i in range (5):
    print (i)
    
for i in range (5):
    print (i)
    print ("hello")
    
string = "Sundevils"

for i in range (len(string)):
    print (i, string[i])
    
lst = [10, 20, 30]
for i in range (len(lst)):
    print (i, lst[i])

for l in lst:
    print (l)
    
    
mylst1 = [10, 20, 30]
mylst2 = [100, 200, 300]

for i in range (len(mylst1)):
    print (i, mylst1[1], mylst2[i])
    
for l1, l2 in zip (mylst1, mylst2):
    print (l1, l2)
    
    
mydictionary = {'A': 100, 'B': 200, 'C': 300}

for k in sorted (mydictionary.keys()):
    print (k, mydictionary[k])
    
for k in reversed(sorted(mydictionary.keys())):
    print (k, mydictionary[k])
    
sumi = 0

for i in range(5):
    sumi = sumi + i
    print (i, sumi)
print (sumi)


P = [10, 20, 30]
sumP = 0

for i in range (3):
    sumP = sumP + P[i]
    print (i, P[i], sumP)
print(sumP)


P = [1, 2, 3]
Q = [10, 20, 30]

sumP = 0
sumQ = 0

for i in range (3):
    sumP = sumP + P[i]
    sumQ = sumQ + Q[i]

print ("P = ", P)
print ("Q = ", Q)
print ("sumP = ", sumP)
print ("sumQ = ", sumQ)


P = [1, 2, 3]
Q = [10, 20, 30]

manhattan = 0
for i in range (3):
    manhattan = manhattan + math.fabs(P[i] - Q[i])

print ("P = ", P)
print ("Manhattan Distance = ", round(manhattan,2))

P = [1, 2, 3]
Q = [10, 20, 30]

manhattan = 0
euclidean = 0
minkowski = 0

for i in range (len(P)):
    manhattan = manhattan + math.fabs(P[i] - Q[i])
    euclidean = euclidean + pow(math.fabs(P[i] - Q[i]),2)
    minkowski = minkowski + pow(math.fabs(P[i] - Q[i]),3)
    
manhattan = pow (manhattan, 1/1)
euclidean = pow (euclidean, 1/2)
minkowski = pow (minkowski, 1/3)

print ("Manhattan Distance = ", round(manhattan,2))
print ("Euclidean Distance = ", round(euclidean, 2))
print ("Minkowski Distance (r=3) = ", round(minkowski,2))


P = [1, 2, 3, 4, 5]
Q = [10, 20, 30, 40, 50]
n = len(P)
sumpq = 0
sump = 0
sumq = 0
sump2 = 0
sumq2 = 0

for p, q in zip(P, Q):
    sumpq += p * q
    sump += p
    sumq += q
    sump2 += pow(p, 2)
    sumq2 += pow(q, 2)
    
nr = (sumpq - (sump * sumq) / n)
dr = (math.sqrt(sump2 - pow(sump, 2) / n) *
      math.sqrt(sumq2 - pow(sumq, 2) /n))
r = nr / dr

print ("P = ",P)
print ("Q = ", Q)
print ("Pearson Correlation = ", round(r,2))

UserRatingsD = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E':5
}

for k in sorted(UserRatingsD.keys()):
    print (k, UserRatingsD[k])
    
    
UserXRatingsD = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E': 5
}

UserYRatingsD = {
    'A':10, 'B':20, 'C':30, 'D':40, 'E':50
}

for k in sorted(UserXRatingsD.keys()):
    print (k, UserXRatingsD[k], UserYRatingsD[k])
    
UserXRatingsD = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E': 5
}

UserYRatingsD = {
    'A':10, 'B':20, 'C':30, 'D':40, 'E':50
}
md = 0
for k in UserXRatingsD.keys():
    md = md + math.fabs(UserXRatingsD[k] - UserYRatingsD[k])

print ("UserXRatingsD = ", UserXRatingsD)
print ("UserYRatingsD = ", UserYRatingsD)
print ("Manhattan Distance = ", round(md,2))

UserRatingsND = {
    'X':{
        'A':10, 'B':20, 'C':30, 'D':40, 'E':50
    },
    'Y':{
        'A':100, 'B':200, 'C':300, 'D':400, 'E':500
    }
}

UserXRatingsD = UserRatingsND['X']
UserYRatingsD = UserRatingsND['Y']

for k in sorted(UserXRatingsD.keys()):
    print (k, UserXRatingsD[k], UserYRatingsD[k])