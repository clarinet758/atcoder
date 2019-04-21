#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
s=input()
t=s.count(".")
for i in s:
    if i=="#": t+=1
    else: t-=1
print(min(t,s.count(".")))
"""

f=[0,1][s[0]=="#"]
b=[0]
w=[0]
for i in s:
    if f==1 and i=="#":
        b[-1]+=1
    elif f==1 and i==".":
        f=0
        if w[-1]!=0: w.append(1)
        else: w[-1]=1
    elif f==0 and i==".":
        w[-1]+=1
    elif f==0 and i=="#":
        f=1
        if b[-1]!=0: b.append(1)
        else: b[-1]=1
x=sum(b)
y=sum(w)
if s[-1]=="#": x-=b[-1]
if s[0]==".": y-=w[0]
#print(b,w,x,y)
ans=min(x,y)
print(ans)

M=s.count(".")
ans=M
for i in range(n):
  if s[i]=="#":
    M+=1
  else:
    M-=1
  ans=min(ans,M)
print(ans)    
"""
