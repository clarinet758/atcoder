#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
ans=[]
for i in s:
    if i=="B" and len(ans): ans.pop()
    elif i in ["0","1"]: ans.append(i)
print("".join(ans))
