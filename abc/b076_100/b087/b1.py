#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a=int(input())
b=int(input())
c=int(input())
x=int(input())
ans=chk=0
for i in range(a+1):
    for j in range(b+1):
        tmp=i*500+j*100
        if x-tmp>=0 and (x-tmp)//50<=c: ans+=1
print(ans)
