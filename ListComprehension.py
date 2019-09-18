list1 = ["python","good","ok","for"]
dict1 = {value:len(value) for value in list1}
print(dict1)


##list1 = [3,7,4,5,6,2,23,90,34]
####list2 = [value*value for value in list1 if value % 2 ==0]
##list2 = [value for value in list1 if value % 2 ==0]
##
##print (list2)
##
####for value in list1: #1
####    if value % 2 ==0: #2
####        print value #3
##
##
####print ([value for value in list1 if value % 2 ==0])
