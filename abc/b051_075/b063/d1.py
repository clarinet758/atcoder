#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,a,b=map(int,input().split())
t=a-b

ans=[0]*2

d=[]
for i in range(n):
    h=int(input())
    d.append(h)
d.sort(reverse=True)
ans[1]=max(d)
while ans[1]-ans[0]!=1:
    x=z=(ans[1]+ans[0])//2
    y=x*b
    for i in range(n):
        p=d[i]-y
        if p<=0:
            break
        x-=(p+t-1)//t
        if x<0:
            break
    if x<0:
        ans[0]=z
    else:
        ans[1]=z
print(ans[1])

