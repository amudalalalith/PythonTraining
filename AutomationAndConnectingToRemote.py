import sys

num1 = sys.argv[1]
num2 = sys.argv[2]
opr = sys.argv[3]

num1 = int(num1)
num2 = int(num2)


if opr == "add":
print num1 + num2
elif opr == "mul":
print num1 * num2




##import subprocess
##output = subprocess.check_output('ipconfig', shell=True)
##
##for line in output.splitlines():
##    if "IPv4 Address" in line:
##        print (line)




##import subprocess
##output = subprocess.check_output('ipconfig',shell=True)
##print (output)




##import subprocess
##output = subprocess.check_output('lscpu', shell=True)
##
##for line in output.splitlines():
##if "Model name" in line:
##speed = line.split()[-1]
##print speed
##break
##
##print output



##import paramiko
##
##list1 = [("10.13.14.56","admin","good5"),("10.13.14.57","admin2","good5"),("10.13.14.58","admin3","good3")]
##
##for data in list1:
##
##ssh = paramiko.SSHClient()
##
##ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##
##hostname1 = data[0]
##username1 = data[1]
##password1 = data[2]
##
##ssh.connect( hostname = hostname1 , port = 22 , username = server1_username, password = password1 )
##
##stdin, stdout, stderr =ssh.exec_command('show version')
##out_put=stdout.read()
##if "5.2.0" not in out_put:
##ssh.exec_command('pip innstall -update paramiko')
##
##stdin, stdout, stderr =ssh.exec_command('show version')
##out_put=stdout.read()
##if "5.2.0" not in out_put:
##print "instalation failed for", data[0]
##
##
##
####import paramiko
####
####
####list1 = [("10.13.14.56","admin","good5","/home/sidique2/"),("10.13.14.57","admin2","good5","/home/sidique2/"),("10.13.14.58","admin3","good3","/home/sidique2/")]
####
####for data in list1:
####
####ssh = paramiko.SSHClient()
####
##ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##
##hostname1 = data[0]
##username1 = data[1]
##password1 = data[2]
##location = data[3]
##
##ssh.connect( hostname = hostname1 , port = 22 , username = server1_username, password = password1 )
##
##stdin, stdout, stderr =ssh.exec_command('ls {}'.format(location))
##out_put=stdout.read()
##print out_put
##
##
##ftp = ssh.open_sftp()
##
##ftp.put('C:\Users\S_Sithiqu\Desktop\my_test\patch.py', '{}/patch.py'.format(location))
##
##ftp.close()
##
##stdin, stdout, stderr = ssh.exec_command('cd /home/siddique;python patch.py')
##out_put=stdout.read()
##print out_put
##
##import paramiko
##
##list1 = [("10.13.14.56","admin","good5"),("10.13.14.57","admin2","good5"),("10.13.14.58","admin3","good3")]
##
##for data in list1:
##
##ssh = paramiko.SSHClient()
##
##ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##
##hostname1 = data[0]
##username1 = data[1]
##password1 = data[2]
##
##ssh.connect( hostname = hostname1 , port = 22 , username = server1_username, password = password1 )
##
##stdin, stdout, stderr =ssh.exec_command('ls /home/siddique/')
##out_put=stdout.read()
##print out_put
##
##
##ftp = ssh.open_sftp()
##
##ftp.put('C:\Users\S_Sithiqu\Desktop\my_test\patch.py', '/home/siddique/patch.py')
##
##ftp.close()
##
##stdin, stdout, stderr = ssh.exec_command('cd /home/siddique;python patch.py')
##out_put=stdout.read()
##print out_put




##f = open('temp.txt','w')
##f.write("fixed")
##f.close()
##
##print "fixed succesfuly" 
##from credentials import *
##
##import paramiko
##
##
##
##ssh1 = paramiko.SSHClient()
##
##ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##
##hostname1 = server1_ip
##username1 = server1_username
##password1 = server1_password
##
##ssh.connect( hostname = hostname1 , port = 22 , username = server1_username, password = password1 )
##
##stdin, stdout, stderr =ssh.exec_command('ls /home/siddique/')
##out_put=stdout.read()
##print out_put
##
##
##ftp = ssh.open_sftp()
##
##ftp.put('C:\Users\S_Sithiqu\Desktop\my_test\patch.py', '/home/siddique/patch.py')
##
##ftp.close()
##
##stdin, stdout, stderr = ssh.exec_command('cd /home/siddique;python patch.py')
##out_put=stdout.read()
##print out_put






##from credentials import *
##
##import paramiko
##
##ssh = paramiko.SSHClient()
##
##ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##
##hostname1 = server1_ip
##username1 = server1_username
##password1 = server1_password
##
##ssh.connect( hostname = hostname1 , port = 22 , username = server1_username, password = password1 )
##
##stdin, stdout, stderr =ssh.exec_command('ls /home/siddique/')
##out_put=stdout.read()
##print out_put
##
##
##ftp = ssh.open_sftp()
##
##ftp.put('C:\Users\S_Sithiqu\Desktop\my_test\patch.py', '/home/siddique/patch.py')
##
##ftp.close()
##
##stdin, stdout, stderr = ssh.exec_command('cd /home/siddique;python patch.py')
##out_put=stdout.read()
##print out_put
