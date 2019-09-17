#Dict CRUD
#key value pair

key_list = [2,3,'Python', '7.2', 10]

value_list = [5,6,7,8]

zip_list = zip(key_list, value_list)

print (list(zip_list))

zip_dict = dict(zip_list)

dict2 = {9:10,11:12, 13:14}

zip_dict.update(dict2)

# merge two dictionaries - zip_list and dict2

print (zip_dict)

'''
dict1 = {1:2, 3: 4, 5: 6,7:8}

dict2 = {9:10,11:12,13:14}

dict1.update(dict2)

print (dict1)

dict1 = {1:2, 3: 4, 5: 6,7:8}

dict1.pop(3)

print (dict1)
'''


'''
key_list = ['a',2,'python','hi',7,78,123,90,78,45,44]
value_list = [5,6,7,8,9,90,67]
zip_list = zip(key_list,value_list)
print(zip_list)
print (dict(zip_list))
'''


'''
dict1 = {}

total = 0

price = {'apple' : 50, 'orange':25, 'lemon':5, 'banana':10}

fruit = ""

while fruit != "done":
    fruit = input("Enter the fruit :")
    if fruit != "done":
        if fruit not in price.keys():
            print ("not available")
        else:
            quantity = input("Enter the Quantity :")
            quantity = int(quantity)
            tot = price[fruit] * quantity
            total = total + tot
        print ("if you complete your purcase, type done")

print ("pls pay {}".format(total))
'''



'''
dict1 = {}

for i in range(5):
    name = input("Enter the name : ")
    mark = input("Enter the mark : ")

    mark = int(mark)

    dict1[name] = mark

print(dict1)

for key,vale in dict1.items():
    if vale >=50:
        print("{} is pass".format(key))
    else:
        print("{} is fail".format(key))

'''


'''
#delete the key
dict1 = {'a':67,8:'good',6:'python'}
del dict1['a']
print(dict1)
'''


'''
#update the value if the key is availabe it will be updated other wise it will be inserted
dict1 = {'a':67,8:'good',6:'python'}
if 'c' in dict1.keys():
    dict1['a'] = 100 # C U
else:
    print("key is not available")

print (dict1)
'''



'''
#creating of the list
dict1 = {}
dict1['a'] = 67
print(dict1)
dict1[6] = "python"
print(dict1)
dict1[8] = "good"
print(dict1)
'''


'''
dict1 = {3:'hi',6:'bye',2:"good",(5,2,8):"python",6.7:90,"a":45,"training":"how"}
#print(dict1.values())
for key,value in dict1.items():
    print ("{} - {}".format(key,value))
'''


'''
dict1 = {3:'hi',6:'bye',2:"good",(5,2,8):"python",6.7:90,"a":45,"training":"how"}

for i in (dict1.keys()):
    try:
        if "tra" in i:
            print (i)
    except:
        pass

#print(dict1.keys())
#print(dict1["training"])
#print (dict1)
'''
