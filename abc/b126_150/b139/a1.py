#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
t=input()
ans=0
for i in range(3):
    ans+=s[i]==t[i]
print(ans)
