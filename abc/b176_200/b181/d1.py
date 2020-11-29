#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


p=set([])
for i in range(111,1000):
    if i%2==0 and ((i//2)%100)%4==0 and "0" not in str(i):
        d=[str(i//100) ,str((i%100)//10) ,str(i%10)]
        d.sort()
        r="".join(d)
        p.add(r)

s=input()
if len(s)<10 and int(s)%8==0:
    print("Yes")
    exit()
if len(s)==2 and (int(s[1])*10+int(s[0]))%8==0:
    print("Yes")
    exit()
w={}
for i in s:
    if i in w:
        w[i]+=1
    else:
        w[i]=1

for i in p:
    if i[0] in w and i[1] in w and i[2] in w:
        w[i[0]]-=1
        w[i[1]]-=1
        w[i[2]]-=1
        if w[i[0]]>-1 and w[i[1]]>-1 and w[i[2]]>-1:
            print("Yes")
            exit()
        w[i[0]]+=1
        w[i[1]]+=1
        w[i[2]]+=1
    
print("No")
