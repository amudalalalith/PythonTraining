import csv

with open('test.csv', 'wb') as csvfile:
    f2 = csv.writer(csvfile, delimiter=',')
    f2.writerow(['name','age','location'])
    f2.writerow(['Kumar','23','chennai'])
    f2.writerow(['Raj','25','Mumbai'])
    f2.writerow(['Priya','21','Pune'])


with open('test.csv', 'rb') as f:
    reader2 = csv.reader(F)

for row in reader2:
    print (row)

##import csv
##
##with open('test.csv', 'rb') as f:
##reader2 = csv.reader(F)
##
##for row in reader2:
##print row[0]
##print row[1]
##print row[2] + "\n"
