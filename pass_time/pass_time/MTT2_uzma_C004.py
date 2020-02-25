import re
import sqlite3 as lite
import sys
in_file = open('emailids.txt')
line=in_file.read()
pattern=re.compile(r'\.com')
pattern1=re.compile(r'\.in')
pattern2=re.compile(r'\.net')
pattern3=re.compile(r'\.edu')
##counts=0
##countr=0
##countt=0
##countf=0
s=pattern.findall(line)
r=pattern1.findall(line)
t=pattern2.findall(line)
f=pattern3.findall(line)
sl=len(s)
print(len(s))
print(len(r))
print(len(t))
print(len(f))

##for pattern in line:
##    counts=counts+1
##print(counts)
##for r in line:
##    countr=countr+1
##print(countr)
##for t in line:
##    countt=countt+1
##print(countt)
##for f in line:
##    countf=countf+1
##print(countf)



















   




