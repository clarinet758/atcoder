#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=chk=0
for i in range(1,n+1,2):
    chk=0
    for j in range(1,i+1):
        if i%j==0: chk+=1
    if chk==8: ans+=1
print(ans)
