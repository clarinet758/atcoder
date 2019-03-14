#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
d=[0]*41
t=[0]*41
p=2**40
x=0
y=1
ans=0
for i,j in enumerate(bin(k)[::-1]):
    if j=="b": break
    if j=="1": d[i]=1
 
for i in a:
    for j,k in enumerate(bin(i)[::-1]):
        if k=="b": break
        if k=="1": t[j]+=1
for i in range(40,-1,-1):
    if d[i]==1 and t[i]>n//2-(n+1)%2:
        y=0
    elif d[i]==1 and t[i]<=n//2:
        x+=p
    elif y==0 and t[i]<=n//2:
        x+=p
    p//=2
for i in a:
    ans+=x^i
print(ans)
