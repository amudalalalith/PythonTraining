class Parent(object):
    def __repr__(self):
        return "siddique"
print Parent()



##class Parent(object):
##def __init__(self):
##print "parent"
##super(Parent, self).__init__()
##
##class Left(Parent):
##def __init__(self):
##print "left"
##super(Left, self).__init__()
##
##class Right(Parent):
##def __init__(self):
##print "right"
##super(Right, self).__init__()
##
##class Child(Right,Left):
##def __init__(self):
##print "child"
##super(Child, self).__init__()
##
##print Child.__mro__ # Method Resolution Order
##
##Child()





##class A(object):
##
##def add(self):
##print "i am from A"
##
##
##class B(object):
##
##def add1(self):
##print "i am from B"
##
##
##class C(B,A):
##
##def add1(self):
##print "i am from C"
##
##
##
##obj = C()
##
##print C.__mro__
##
##obj.add()




##class A():
##    def add(self,x,y):
##        print (x+y)
##
##class B():
##    def add(self,x,y):
##        print (x*y)
##
##class C(A,B):
##    def sub(self,x,y):
##        print (x-y)
##
##obj = C()
##print(C.__mro__)
##obj.sub(6,3)
##obj.add(6,3)




##class A(object):
##    def add(self,x,y):
##        print (x+y)
##
##class B(object):
##    def mul(self,x,y):
##        print (x*y)
##
##class C(A,B):
##    def sub(self,x,y):
##        print (x-y)
##
##obj = C()
##obj.sub(6,3)
##obj.add(6,3)
##obj.mul(6,3)



##class A():
##    var1 =5
##    def __init__(self):
##        self.var2 = 10
##
##    def sample(self,x):
##        print("I am an object method")
##
##    @classmethod
##    def class_sample(cls,y):
##        print(cls.var1)
##        print("I am a class method")
##
##    @staticmethod
##    def static_sample(z):
##        print("I am static method")
##
##
##obj = A()
##A.sample(5)
##obj.class_sample(10)
##
##obj.static_sample(78)
##
##A.static_sample(56)




##class Parent():
##    def _protected(self):
##        print ("protected")
##
##    def __private(self):
##        print ("private")
##
##    def sample(self):
##        print ("i am public")
##
##obj = Parent()
##
##obj.sample()
##obj._protected()
##obj.__private()
##



##class Sample():
##    def __init__(self):
##        self.public = 5
##        self._protected = 10
##        self.__private = 15
##
##    def test(self):
##        print (self.public)
##        print (self._protected)
##        print (self.__private)
##
##
##obj1 = Sample()
##
##print (obj1.public)
##print (obj1._protected)
##print (obj1.__private)



##class Sample():
##    total = 0
##    def __init__(self,name,mark1,mark2):
##        Sample.total = Sample.total + 1
##        self.name = name
##        avg = (mark1 + mark2) / 2.0
##        self.avg = avg
##    
##    def result(self):
##        if self.avg >= 50:
##            print ("pass")
##        else:
##            print("fail")
##    
##obj = Sample("Kumar",56,78)
##print (Sample.total)
##print (obj.name)
##obj1 = Sample("Priya",45,32)
##print (Sample.total)
##print (obj1.name)




##init method
##class Sample():
##    def __init__(self,name,mark):
##        self.name = name
##        self.mark = mark
##        print("Marks",self.name)
##    
##    def result(self):
##        if self.mark >= 50:
##            print ("pass")
##        else:
##            print("fail")
##    
##obj = Sample("Kumar",56)
##obj1 = Sample("Priya",45)
##
##obj.result()
##obj1.result()





##class Sample():
##    def test1(self,x):
##        self.x=x
##        print ("I am test1")
##    def test2(self):
##        print("I am test2")
##obj = Sample()
##obj1 = Sample()
##obj2 = Sample()
##obj.test1(5)
##obj1.test1(100)
##obj2.test1(67)
##
##print(obj.x)
##print(obj1.x)
##print(obj2.x)




##class Sample():
##    def test1(self,x):
##        print ("I am test1")
##        print(x)
##    def test2(self):
##        print("I am test2")
##obj = Sample()
##obj.test1(5)
