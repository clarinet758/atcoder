#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
s=input()
d=[[30005,-1] for i in range(10)]
ans=set([])
for i in range(n):
    p=int(s[i])
    if d[p][0]==30005:
        d[p][0]=i
        d[p][1]=i
    else:
        d[p][1]=i

for i in range(1,n-1):
    for j in range(10):
        if d[j][0]<i:
            for k in range(10):
                if d[k][1]>i:
                    ans.add(str(j)+str(s[i])+str(k))
        
print(len(ans))
