#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


s=input()
t=input()
x=len(t)
ans=chk=x
for i in range(len(s)-len(t)+1):
    chk=x
    for j in range(x):
        chk-=s[i+j]==t[j]
    ans=min(ans,chk)
print(ans)
