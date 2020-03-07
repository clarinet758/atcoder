#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def chk(j,k):
    s=set([i for i in str(j)])
    if len(s)<=k: return 1
    else: return 0

o=999999999999999999
a,k=map(int,input().split())
l=[int(i) for i in "0"+str(a)]

# x>a y<a
x=v=0
y=1
if chk(a,k):
    print(0)
    exit()
for i,j in enumerate(str(a)):
    i+=1
    c=v*10
    v=c+l[i] #n_base
    x1,y1=x*10,y*10
    x=y=o
    for t in range(10):
        if chk(x1+t,k):
            if abs(x1+t-v)<abs(x-v) and x1+t>v: x=x1+t
        if chk(c+t,k):
            if abs(c+t-v)<abs(x-v) and c+t>v: x=c+t
        if chk(y1+t,k):
            if abs(y1+t-v)<abs(y-v) and y1+t<v: y=y1+t
        if chk(c+t,k):
            if abs(c+t-v)<abs(y-v) and c+t<v: y=c+t
    
print(min(abs(x-a),abs(y-a)))
