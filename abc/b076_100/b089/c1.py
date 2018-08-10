#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
d={"M":0,"A":0,"R":0,"C":0,"H":0}
t=["M","A","R","C","H"]
ans=chk=0
for i in range(n):
    s=input()
    if s[0] in d:
        d[s[0]]+=1
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            ans+=d[t[i]]*d[t[j]]*d[t[k]]
print(ans)
