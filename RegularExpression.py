import re

str1 = r"""
hi how3 arekarthik@aricent.com you6
2 i am \fine
# how about sithiqu.mtech@gmail.com you
334354 i am f$ine
@ how about sithiqu.mtech@gmail.com you
& i am $fine
33435443643 how about sithiqu.mtech@gmail.com you
how python you
Pythn \you
4 i too fine"""
#(+ ? . * ^ $ ( ) [ ] { } | \)

pattern = re.compile(r"you")
#pattern = "^Sun [1][5,6,7]:[0-5][0-9].*"
#pattern = ".*(([0-9|A-F]{2})-){5}[0-9|A-F]{2}.*"
#pattern = r".*\\.*"
#pattern = re.compile(r".*\\.*")
#pattern = ".*\$.*"
#"([2,3,4,5]|[a,c,i]){2}"
#pattern = "^."
#pattern = ".*pytho*n.*"
#pattern = ".*pytho+n.*" #one or more
#pattern = ".*pytho?n.*" #either or 
#pattern = ".*python.*"
#pattern = "^[@#&3]"
#pattern = "^[1,4,7]"
#pattern = ".*[4-5].*"
#pattern = ".*[\d]$"#end with
#pattern = "^[\d]{10,} "
#pattern = "^[\d]{,10} "
#pattern = "^[\d]{10,12} "
#pattern = "^[\d] "
#pattern = ".*[\d]"
for line in str1.splitlines():

    #out_put = re.search(pattern, line,re.I)
    out_put = re.match(pattern, line)
    
    if out_put:
        print (line)
        #print (out_put,line)
