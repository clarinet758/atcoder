#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=input()
ans=0
chk=""
for i in n:
    if chk=="" or chk[-1]==i:
        chk+=i
    else:
        chk=chk[:-1]
        ans+=2
    
print(ans)
