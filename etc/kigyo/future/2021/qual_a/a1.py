#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

h=w=0
s=""
m=[]
car=[-1]*100
for i in range(100):
    a,b=map(int,input().split())
    if a%2: m.append((a,-b,i))
    else: m.append((a,b,i))
m.sort()

for p,q in enumerate(m):
    a,b,c=q
    b=abs(b)
    car[p]=c
    if h<a:
        s+="D"*(a-h)
    elif h>a:
        s+="U"*(h-a)
    
    if w>b:
        s+="L"*(w-b)
    elif w<b:
        s+="R"*(b-w)
    s+="I"
    h,w=a,b
if h<10:
    s+="D"*(10-h)
elif h>10:
    s+="U"*(h-10)
if w>10:
    s+="L"*(w-10)
elif w<10:
    s+="R"*(10-w)
h=w=10
bara={}
for i in range(10):
    for j in range(10):
        p=car.pop()
        if i%2: bara[p]=((h+i,19-j))
        else: bara[p]=((h+i,w+j))
        if j<9: s+=["OR","OL"][i%2]
        else: s+="O"
    if i<9: s+="D"
#print(bara)
h,w=19,10
for i in range(100):
    a,b=bara[i][0],bara[i][1]
    if h<a:
        s+="D"*(a-h)
    elif h>a:
        s+="U"*(h-a)
    
    if w>b:
        s+="L"*(w-b)
    elif w<b:
        s+="R"*(b-w)
    s+="I"
    h,w=a,b
print(s)


    
"""
for i in range(1):
    if h<a:
        s+="D"*(a-h)
    elif h>a:
        s+="U"*(h-a)
    
    if w>b:
        s+="L"*(w-b)
    elif w<b:
        s+="R"*(b-w)
    s+="I"
    h=a
    w=b
print(s)
"""
