#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,l=map(int,input().split())
ans=0
chk=10000
for i in range(n):
    ans+=i+l
    if abs(chk)>abs(i+l):
        chk=i+l
print(ans-chk)
