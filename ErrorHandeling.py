a= input("enter the valid mark : ")
a= int(a)
try:
    if (a>=0) and (a<=100):
        print ("your  good")
    else:
        raise Warning("this is not the valid error")
except Warning as var:
    print(var)


'''
a= input("enter the valid mark : ")
a= int(a)

#print (a>=0) and (a<=100)
assert (a>=0) and (a<=100)

print ("your good")
'''

'''
var = input("Enter the name:mark : ")

var2 = var.split(':')
try:
    name = var2[0]
    mark = var2[1]
    mark = int(mark)
    #z = 2/0 # will be shown in the last except
except IndexError as err1:
    print (err1)
    print("please provide the valid input")
except ValueError as err2:
    print (err2)
    print("please provide the valid numbers in the mark")
except:
    print("Unknown error")
else:
    if mark > 50:
        print ("{} is pass".format(name))
    else:
        print ("{} is fail".format(name))
'''
    



'''
print ("Hi")
try:
    print (var)
except Exception as err:
    print (err)
    print ("its error") # if try has invalid code then except and finally will get executed or else try, else and finally will get executed.
else:
    print ("i am from else")
finally:
    print("i am from finally")
print ("bye")
'''
