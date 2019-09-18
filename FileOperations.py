with open('sample4.txt','r') as f1, open('sample2.txt','w') as f2:
    var = f1.read()
    f2.write(var)


'''
f = open('sample2.txt','r+')

f.seek(20)
var = f.read()

var1 = var.replace("java","python")

f.seek(20)
f.write(var1)

f.close()
'''

'''
f = open('sample4.txt','w+')

f.write("hi\n")
f.write("how are you\n")
f.write("i am fine\n")
f.write("good\n")

print(f.tell())

f.seek(0)

#var = f.read()
#print (var)



#for line in f.readlines():
#    print(line)

f.close()
'''

'''
f = open('sample2.txt','r')

for i in range(7):
    print(f.readline())
        
f.close()
'''


'''
f = open('sample2.txt','r')

for i in range(100):
    print(f.readline())

f.close()
'''

'''
f = open('sample2.txt','r')

f.seek(30)

var = f.read()
print(var)

print (f.tell())

f.close()
'''

'''
f = open('sample2.txt','w')

f.write("hi\n")
f.write("how are you\n")
f.write("i am fine\n")
f.write("how about you\n")
f.write("i too fine\n")

f.close()
'''
