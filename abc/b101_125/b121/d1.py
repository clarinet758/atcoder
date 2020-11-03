#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b=map(int,input().split())
w=[0]*50
p,q=[0]*50,[0]*50
ans=0
t=1

for i in range(50):
    x=(b+1)//(t*2)
    q[i]=t*x
    if (b+1)%(t*2)>t: q[i]+=(b+1)%(t*2)-t
    t*=2
    if t>b: break

t=1
for i in range(50):
    x=a//(t*2)
    p[i]=t*x
    if a%(t*2)>t: p[i]+=a%(t*2)-t
    t*=2
    if t>a-1: break
t=1
for i in range(50):
    ans+=abs(p[i]-q[i])%2*t
    t*=2
print(ans)
