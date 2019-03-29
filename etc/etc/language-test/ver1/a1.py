#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

input()
s=input()
ans=[0]*4
for i in s:
    ans[ord(i)-ord("1")]+=1
print(max(ans),min(ans))
