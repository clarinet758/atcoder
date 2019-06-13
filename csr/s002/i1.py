#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[]
d=[1]*n
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
for i in range(n):
    if d[i]==0: continue
    a,b=l[i]
    f=1
    for j in range(n):
        x,y=l[j]
        if i==j:
            pass
        elif (a+y-1)//y>(x+b-1)//b or (a//y==x//b and a%y>0 and x%b==0):
            d[j]=0
        else:
            f=0
            break
    if f:
        print(i+1)
        exit()
print(-1)
