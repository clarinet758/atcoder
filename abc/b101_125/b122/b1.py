#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

d={"A","C","G","T"}
ans=chk=0
s=input()
for i in s:
    if i in d:
        chk+=1
        ans=max(ans,chk)
    else:
        chk=0
print(ans)
