





'''
x = 1

x += 1 # x = x + 1

print (x)
'''


'''
var1 = "i am python"
if "python" not in var1: #if var1:
    print ("ok")
else:
    print("Not Ok")
'''



'''
#flags
var1 = None
var2 = True
var3 = False
print(type(var1))
print(type(var2))
print(type(var3))

if var1:
    print ("ok")
else:
    print("Not Ok")

if var2:
    print ("ok")
else:
    print("Not Ok")

if var3:
    print ("ok")
else:
    print("Not Ok")
'''

#print(dir(str))


'''
var = [5,6]
if isinstance(var,set):
    print ("its set")
else:
    print ("it is not a set")
'''

'''
var1 = "hi how are you i am fine"
print (var1.count('i'))
print(var1.index('i'))
print(len(var1))
'''


'''
var1 = "56a"
if var1.isdigit() == True:
    var2 = int(var1)
    print (var2)
'''

'''
var1 = """i am java
java is good
hi how are you
java training"""

var1 = var1.replace("java","python")
print (var1)
'''

'''
var2="12PYTHON9324"
var2=var2.strip('12324P')
print (var2)
'''


'''
var1 = "python"
var2 = "PYTHON"

var1 = var1.lower()
var2 = var2.lower()

if var1 == var2:
    print("OK")
else:
    print("not ok")
'''


'''
var1 = "python"
var2 = "000000python000000"

var2 = var2.strip('0')

if var1 == var2:
    print("OK")
else:
    print("not ok")
'''

'''
#Test case 1 TC1
var = """TC_1 is executed and its fail
TC_2 is executed and its pass
TC_3 is executed and its fail
TC_4 is executed and its pass
TC_5 is executed and its pass
TC_6 is executed and its fail
TC_7 is executed and its pass"""
for line in var.splitlines():
    if "pass" in line:
        print (line.split()[0])
'''


'''
#multiline string
var = """hi how are you
i am fine
how about you
i am good"""

var2 = var.splitlines()
print (var2)
'''

'''
#swap
ip = "10.198.34.78"
var1 = ip.split('.')
var1[2],var1[3] = var1[3],var1[2]
var1 = '.'.join(var1)
print(var1)
'''

'''
var1 = ["hi","how","bye"]

var2 = ' '.join(var1)

print(var2)
'''


'''
var = "I am fr&om mum&bai"

#var2 = var.split('&')
var2 = var.split('&',1)
#print (var2[-1])
print(var2)
'''
