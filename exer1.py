import re

f=open('test.txt')
# pattern=r'[A-Z]\w*'
pattern=r'-?\d+\.?/?\d*%?'
l=[]
for line in f.readlines():
    l+=re.findall(pattern,line)

print(l)