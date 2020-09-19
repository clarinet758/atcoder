#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
ans=0
if n<3:
    print(0)
    exit()
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            chk=[l[i],l[j],l[k]]
            chk.sort()
            if chk[0]+chk[1]>chk[2] and chk[0]!=chk[1] and chk[1]!=chk[2]:
                ans+=1
print(ans)
