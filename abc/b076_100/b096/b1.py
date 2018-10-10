#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
l=[int(i) for i in input().split()]
k=int(input())
ans=chk=0
for i in range(3):
    tmp=l[i]
    for j in range(k):
       tmp*=2
    ans=max(ans,sum(l)+tmp-l[i])
print(ans)
