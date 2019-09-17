
from sys import getsizeof
var1 = 'a'
var2 = 'ab'
var4 = 'abc'
var3 = 5
print (getsizeof(var1))
print (getsizeof(var2))
print (getsizeof(var4))
print (getsizeof(var3))


'''
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print (x1 is y1)
print (x3 is y3)
'''


'''
list1 = [4,7,3,9]

list2 = [4,7,3,9]

print id(list1[0])

print id(list2[0])

list1[0] = 'a'

print list1
print list2

print id(list1[0])

print id(list2[0])

list1 = [4,7,3,9]

list2 = list1

list1[0] = 'a'

print list1

print list2
'''

'''
list1 = [4,7,3,9]
list2 = [4,7,3,9] # list1 = list2

list1[0] = 'a'
print (id(list1[1]))
print (id(list2[1]))
'''


'''
var1 = 5

var2 = 5

print (id(var1))

print (id(var2))

list1 = ['a',6,12,5]

print (id(list1[3]))
print (id(list1[2]))
print (id(list1))
'''


'''
var1 = 5
#run time stack mem - var1 - holds the pointer
#heep mem 5
var2 = 5
print (id(var1))
print (id(var2))
'''

'''
list1 = [4,7,3,9]
list2 = list1

list[0] = 'a'
print (list1)
print (list2)
'''
