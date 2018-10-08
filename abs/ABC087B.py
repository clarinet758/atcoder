#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a=int(input())
b=int(input())
c=int(input())
x=int(input())
ans=0
for i in range(a+1):
    for j in range(b+1):
        tmp=x-(i*500+j*100)
        if 0<=tmp and tmp//50<=c: ans+=1
print(ans)
#
#変則な書き方が思いつかない
