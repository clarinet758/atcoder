#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(input()) for i in range(n)]
ans=[]
ans.append(l[0])
for i in range(1,n):
    f=1
    for j in  range(len(ans)):
        if l[i]<=ans[j]:
            ans[j]=l[i]
            f=0
            break
    if f:
        ans.append(l[i])
    ans.sort()
print(len(ans))
