#No code Exists
from functools import reduce
def op(x,y):
    print(x,end='@@')
    if x!=None:
        print(x*y)  #x[y] can take with out return the x[y]
        return x
l1 =[2,2]
l2=[3,4]
a = reduce(op,l1,l2)
b = reduce(lambda x,y:x*y,l1,l2) # we cant take for list in lambda as x[y] by default it returns x[y] is int then
# for int we cant perform x[y]
# #print(b)
#=======================================================================
from functools import reduce
obj = {"a":{"b":{"c":{"d":1}}}}
l = "a.b.c.d".split(".")
a = reduce(lambda x,y:x[y],l,obj)
print(a)
#=======================================================================
#palindrome
s = input("Eneter the string")
for i in range(0,len(s)):
    if s[i]!=s[-1-i] :
        print(f"{s} is not a arm storng")
        break
print(f"{s} is Armstrong")
#=======================================================================
#decorators
def decor(fun):
    def inner(name,age):
        if age<18:
            print(f"{name} ur not eligible")
        else:
            fun(name,age)
    return inner
@decor
def wish(name,age):
    print(f'{name} whats happening')
wish("durga",3)
#==========================================================================================
#chaining decorators
def decor(func):
    def inner(name):
        print("First Decor(decor) Function Execution")
        func(name)
    return inner

def decor1(func):
    def inner(name):
        print("Second Decor(decor1) Execution")
        func(name)
    return inner

@decor
@decor1
def wish(name):
    print("Hello",name,"Good Morning")

wish("Durga")

#==========================================================================================
#loggers
import logging
logger = logging.getLogger("First")
logger.setLevel(logging.ERROR)
file = logging.FileHandler("abc.txt",'w')
file.setLevel(logging.ERROR)
format = logging.Formatter('%(asctime)s-%(name)s-%(message)s-%(levelname)s',"%d-%m-%y %H:%M:%S")
file.setFormatter(format)
logger.addHandler(file)
logger.error("critical")
#================================================================================================
#nof words,lines,characters in a file
with open("sample.txt") as f:
    a = f.read().split("\n")
    ccount,wcount,lcount=0,0,0
    lcount=len(a)
    for i in a:
        wcount+=len(i.split(" "))
        ccount+=len(i)
    print("words:",wcount)
    print("lines:", lcount)
    print("characters:",ccount)
#=====================================================================================================
#copying of file
from shutil import copyfile
copyfile("sample.txt", "sample_copy.txt") #copyfile(source,destination)
#=======================================================================================================
#dictionary reader/writer
import csv

op = open("samplecsv.csv", "r")
dt = csv.DictReader(op)
print(dt)
up_dt = []
for r in dt:
	print(r)
	row = {'NAME': r['NAME'],
		'AGE': r['NAME'],
		'MARKS': 99}
	up_dt.append(row)
# print(up_dt)
op.close()
op = open("sample.csv", "w", newline='')
headers = ['MARKS', 'AGE', 'NAME']
data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
data.writeheader()
data.writerows(up_dt)

op.close()
#===============================================================================================
#comprehension
l = [[1,2,3],[4,5,6]]

a = [ i1 for i in l for i1 in i if i1%2==0]
print(a)
#################
l = [1,2,3]
a = list(map(lambda x:x*2 if x%2==0 else None,l))
print(a)
#===============================================================================================
res = input("enter string:")
# d={}
# res=''
# for key in st:
#     if key in d.keys():
#         d[key]+=1
#     else:
#         d[key]=1
# for k,v in d.items():
#     res = res +k +str(v)
# print(res,len(st))
temp=''
num=0
chr=''
out =''
for i in range(len(res)):
    if res[i].isalpha() or i==len(res)-1:
        # if i < len(res) - 1:
        if res[i].isnumeric():
            num = num+res[i]
        a = int(num)
        print(chr * a, end='')
        out = out +(chr*a)
        temp = res[i]
        chr=res[i]
        num=''
    elif res[i].isnumeric():
        num = num+res[i]
print(len(out))
#===============================================================================================================
# mobile = input("Enter Number:")
# pattern = re.compile('0?(91|\+91)?[6-9](\d){9}')
# match = pattern.fullmatch(mobile)
# print(match)
# for i in match:
#     print(i)
# import re
# a = urlopen('https://www.redbus.in/info/contactus')
# f = str(a.read())
# l = re.finditer("(91|\+91)?\d{10}",f)
# for i in l:
#     print(i)
# pattern = re.compile("\+91\d{10}")
# l = pattern.findall(f)
# print(l)
#=========================================================================
#files in a direstory using regex
import os
import re

rootdir = "C:\\Users\prasaka\PycharmProjects\Learning200421"
regex = re.compile('.+\.(py)$')
for root, dirs, files in os.walk(rootdir):
  for file in files:
    if regex.match(file):
       print(file)
#;===================================================================================
#Database connectivity
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
query = 'create table employees (name varchar2(20),empid number)'
cur.execute(query)
query_insert = 'insert into employees values(?,?)'
cur.executemany(query_insert,[["durga",414],["vamsi",981]])
con.commit()
cur.execute("select * from employees")
print(cur.fetchall())
cur.close()
con.close()
#{"name":"durga","empid":2759},{"name":"suresh","empid":981}
#===============================================================================



