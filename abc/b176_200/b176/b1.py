#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
ans=chk=0
for i in s:
    chk+=int(i)%9
    chk%=9
print("Yes" if chk==0 else "No")
