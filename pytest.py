# Data structures in python & its hows:
# 1. Array
# 2. List
# 3. Tuple
# 4. Dictionary
# 5. 2D ARRAY
# 6. Matrix
# 7. Set


import numpy as np
from array import *

#------------------------------ARRAYs----------------------------------

#init
arr = array('d',[1.2,2,3])
for i in arr:
	print(i)

# accessing array element
print(arr[2])
print('\n')



#insertion 
arr.insert(1,3)

#printing
for i in arr:
	print(i)


#delete
del arr[1]
print('\n')

#printing
for i in arr:
	print(i)

#search elements index
# when not it returns an error
print('\n')
print(arr.index(2))


#update
arr[0] =1
print('\n',arr)


#---------------------------LISTs--------------------------------

#init
l = []
list1 = [1,"english",2,3,4,5] 
print(l,list1)

#accessing
print(list1[2:len(list1)])

#updating
list1[1] =.5
print(list1)

#delete
del list1[1]
print(list1) 


#-----------------------TUPLE----------------------------

#init
tup = ()
tup1 = (1,2,3,4,)

#accessing
print(tup1[1])

# can't update
#tup1[1]=3

#not even del an element, to delete, delete entire tuple
#del tup1[1]


#--------------------DICT------------------------------

#init
dic = {}
dic1 = {10:'apple', 2:'ball'}

#accessing vals in dict
for x in dic1:
	print("hi",dic1[x])

# insert
dic1[3] = 'cat'	
#accessing vals in dict
for x in dic1:
	print("hi",dic1[x])

#update
dic1[10] = 'apple inc'

print(dic1[10])

#del
del dic1[10]

dic1['banana'] =2
print(dic1)


#--------------------2D ARRAY------------------------------
#init
arr1 =[[1,2,3],[4,5,6,7]]
print(arr1)

#accessing
print(arr1[1])
print(arr1[0][1])

for r in arr1:
	for c in r:
		print(c, end=" ")
	print("$")

#update value

arr1[0][0]=0
print(arr1[0][0])

#del
del arr1[1]
print(arr1)		


#-------------------MATRIX----------------------------
# EVERY MATTRIX IS A 2D ARRAY BUT NOT VICE-VERSA
#init
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
# non-inplace
arr3 = arr2.reshape(3,2)
print(arr3)
# inplace
arr2.shape = (3,2)
print(arr2)

########## adding a row ##########
#axis=0 keeps the shape, otherwise flattens
# no inplace option, not efficient 
arr5 = np.append(arr2,[[7,8]],axis=0)
print(arr5)


######### adding a column #########
arr6 = np.insert(arr5,[2],[ [9],[10],[11],[12] ],1)
print(arr6)


#-------------------SETs-----------------------

#init
sets = set([1,2,3])
print(sets)

#add
sets.add("mon")

print(sets)

sets.discard("mon")

print(sets)

#union
sets2= set(['a','b','c'])
sets3 =sets|sets2
print(sets3)

#interset
sets4 = sets&sets3
print(sets4)