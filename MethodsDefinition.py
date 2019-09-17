
#local variable and global variable
global sum2
sum2 = 800
def total(a,b,c,d,e):
    global sum1
    sum1 = a + b + c + d + e
    print (sum1, " from total")
    sum2 = 600
    print (sum2, "sum 2")
    
def average(name):
    print (sum1, " from average")
    avg = sum1 / 5
    print ("average mark of {} is {}".format(name,avg))
    avg1 = sum2/5
    print ("average mark of sum2 is {}".format(avg1))

total(56,34,78,90,23)

average("Kumar")



'''
list1=["kumar",23,"chennai"]
def data(name,age=False,location=False):
    print (name,age,location)

data(list1[0])
#data(*list1)
#data(list1[0],list1[1],list1[2])
'''

'''
def shop(**var):
    total = 0
    price = {'apple':50,'orange':15,'lemon':5}
    for fruit,qty in var.items():
        tot = price[fruit] * qty
        total = total + tot
    print (total)

shop(apple=3,orange=4,lemon=5)
shop(apple=3)
shop(apple=3,orange=4)
'''


#passing arguments as key value pair
'''
def test(name,**kvargs):
    print (name)
    print (kvargs)

test("kumar", english=[67,7,8,9],hindi="a",maths=90)
test("Raj", english=67)
test("kumar")
test("kumar", english=67,hindi=45)
'''


'''
def test(name,*args):
    list1 = list(args)
    print (name)
    print (list1)


test("kumar",67,34,78,89)
test("kumar",67)
test("kumar")
'''

'''
def mysort(name,*args):
    print (name)
    print (args) #saved as a tuple

mysort('kumar',45,67,89)
'''


'''
var =[90,56,2,7,21,11,3]
def mysort(list1,flag=False):
    if flag == "reverse":
        return sorted(list1,reverse=True)
    else:
        return sorted(list1)

print (mysort(var))
print (mysort(var,"reverse"))
'''


'''
def test(x,y=3):
    mysum = x+y
    return mysum,x

#var1,var2 = test(5,6)

#print (var1, var2) #print(test(5,6))
print(test(5))
'''

'''
def test(x):
    if x%2 == 0 :
       return "even"
    else:
       return "odd"

for i in range(5):
 var1 = input("enter number:")
 y = int(var1)
 print (test(y))
'''
