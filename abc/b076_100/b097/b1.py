#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
x=int(input())
ans=chk=1
for i in range(x):
    for j in range(2,11):
        chk=i**j
        if chk<=x: ans=max(ans,chk)
    
print(ans)
