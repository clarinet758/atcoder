#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


s=input()
ans=chk=0
for i in s:
    if i in "ACGT": chk+=1
    else: chk=0
    ans=max(ans,chk)
print(ans)
