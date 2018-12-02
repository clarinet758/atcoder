#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
x=input()
ans=cnt=0
for i in x[::-1]:
    if i=="T": cnt+=1
    if i=="S" and cnt>0:
        cnt-=1
        ans+=2
print(len(x)-ans)
