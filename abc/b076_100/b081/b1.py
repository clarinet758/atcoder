#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
ans=40
for i in a:
    tmp=0
    while i%2==0 and tmp<ans:
        i//=2
        tmp+=1
    ans=min(ans,tmp)
print(ans)
