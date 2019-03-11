#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

p=[0]*42
q=[0]*42
x=1
a,b=map(int,input().split())
if a==b:
    print(a)
    exit()

a-=1
for i in range(42):
    if b//x<1: break
    if x==1:
        q[0]=((b+1)//2)%2
    else:
        q[i]=[0,((b+1)%x)%2][(b//x)%2]
    x*=2
x=1        
for i in range(42):
    if a//x<1: break
    if x==1:
        p[0]=((a+1)//2)%2
    else:
        p[i]=[0,((a+1)%x)%2][(a//x)%2]
    x*=2
x=1
ans=0
for i in range(42):
    ans+=(p[i]^q[i])*x
    x*=2
print(ans)
