# CRUD for List
#>>>print(dir(list))
#>>>help()
#>>>list



'''
list1 = [5,8,3,2,90,6]

print (min(list1))
print (max(list1))
print (sum(list1))
print (len(list1))
'''


'''
#Empty List
list1 = [None] * 10 #Empty list with 10 use None
#list1 = []
list1.insert(4,"hi")
print(list1)
'''


'''
#list to set to remove duplicates
list1 = ['a','b','c','d','b','e']
list2 = set(list1)
list2 = list(list2)
print(list2)
print (sorted(list2))
'''


'''
list1 = ['a','b','c','b','d','b','e','b','f']

count = list1.count('b')

for i in range(count):
    if i != 0:
        list1.remove('b')

print (list1)

'''

'''
#Finding minimum

list1 = [31,53,56,6,8,2,18,44,21]

temp = list1[0]

for i in list1:
    if temp < i:  #for min temp < i
        temp = i

print ("max is",temp,"from",list1) 
'''


'''
#Sorting
list1 = [5,2,9,12,89,34,21,76,32,90,53]
list1.sort()
print(list1)
'''


'''
list1 = [5,2,9,12,89,34,21,76,32,90,53]


lprint (sorted(list1,reverse=True))

print (list1)

list1.sort(reverse=True)
print (sorted(list1,reverse=True))

print (list1)
'''


'''
#Merge the two lists

list1 = ['a','b','c','d','b','e']
list2 = [2,3,4]

#list1.extend(list2) #['a', 'b', 'c', 'd', 'b', 'e', 2, 3, 4]
list1.append(list2) #['a', 'b', 'c', 'd', 'b', 'e', [2, 3, 4]]

print(list1[6][1])
'''


'''
#find index of letter
list1 = ['a','b','c','d','b','e']
countofvar = list1.count('b')
print(countofvar)
for i in range(countofvar):
    list1.remove('b')
    print(list1)
'''


'''
#value based removing
list1 = ['a','b','c','d','b','e']
list1.remove('b')
print(list1)
'''

'''
#value based removing via pop
list1 = ['a','b','c','d','e']
list1.pop(1)
print(list1)
'''

'''
#value based removing via pop
list1 = ['a','b','c','d','e']
list1.pop()
print(list1)
'''

'''
#value based removing
list1 = ['a','b','c','d','e']
list1.remove('b')
print(list1)
'''

'''
#sequence 
seq = range(25,50)
list1 = []

for i in range(10):
    var = input("enter the datapacket sequence no : ")
    var = int(var)
    list1.append(var)
for value in list1:
    if value in seq:
        print (value)
'''

'''
sub = ["English","Hindi","Maths"]
list1 = []
name = input("Enter the name : ")
for i in sub:
    mark = input("Enter the mark for {}: ".format(i))
    mark = int(mark)
    list1.append(mark)
'''


'''
list1 = []
name = input("Enter the name : ")
for i in range(5):
    mark = input("Enter the mark : ")
    mark = int(mark)
    list1.append(mark)

total = sum(list1)

avg = total/len(list1)

print ("{} scored {} and his/her average is {}".format(name,total,avg))
'''



'''
#delete operation
list1 = ['a','b','c','d']
del list1[2]
print (list1)
list2 = ['a','b','c','d','e']
del list2[2:4]
print (list2)
'''

'''
#updating the element
list1 = ['a','b','c','d']
list1[2:4] = ('y','x')
print (list1)

list1 = ['a','b','c','d']
list1[2] = "python"
print (list1)
'''



'''
#inserting in to list
list1 = ['a','b','c','d']
list1.insert(2,"python")
print (list1)
'''

'''
#appending

list1 = []
print(list1)
list1.append('a')
print(list1)
list1.append('b')
list1.append('c')
print(list1)
'''


'''
list1 = ['a','b','c','d','e','f','g','h','i','j']

print(list1[::2])#print skipping the second elemnt
print(list1[:6])
#print(list1[::-1) # reverse the list
#print(list1[-4])
#print(len(list1))
#print(list1[2:8:3])
'''

'''
list1 = ['a','b','c','d',(5,2,8,9),'e','f']

print (type(list1))
print (type(list1[4]))

"{} is pass".format(name)
'''
