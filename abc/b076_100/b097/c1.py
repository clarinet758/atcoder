#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
k=int(input())
n=len(s)
d=set()
#d={s[i:j+1] for j in range(i,n) for i in range(n)}
#d={s[i:j+1] for i in range(n) for j in range(i,n)}
for i in range(n):
    for j in range(i,max(n,i+5)):
        d.add(s[i:j+1])
ans=sorted(list(d))
print(ans[k-1])
