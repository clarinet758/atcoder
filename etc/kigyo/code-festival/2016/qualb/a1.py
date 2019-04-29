#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

w="CODEFESTIVAL2016"
s=input()
ans=0
for i in range(16):
    if w[i]!=s[i]: ans+=1
print(ans)
