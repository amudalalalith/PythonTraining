list1 = [(4,2),(8,5),(7,0)]
print(list(map(lambda x,y : x * y,list1,list1)))


##import functools
##list1 = [5,3,6,7,8,1,2,56,23]
##print (int(functools.reduce(lambda x,y : x + y,list1)))


##list1 = [5,3,6,7,8,1,2,56,23]
##
##
##my_fun = lambda x,y,z : x * y * z
##
##
##print (my_fun(4,5,6))
##list1 = [5,3,6,7,8,1,2,56,23]
##
##
##my_fun = lambda x,y,z : x * y * z
##
##print (my_fun(4,5,6))



##list1 = [4,2,8,5,7]
##
##print (list(map(lambda x : x * x,list1)))



##list2 = [(2,3),(3,5)]
##print (list(map(lambda (x,y) : x + y,list2))) # not work



####def my_sqr(x):
####    return x*x
####my_sqr = lambda x : x*x
####print (map(my_sqr,list1))
