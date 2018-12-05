#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()
d=[set(i) for i in s]
ans=0
for i in range(101):
    if len(d)==1: break
    tmp=d[0]
    for  j in range(1,len(d)):
        tmp=tmp&d[j]

    if len(tmp)>=1: break
    for j in range(len(d)-1):
        d[j]=d[j]|d[j+1]
    d.pop()
    ans+=1
print(ans)
