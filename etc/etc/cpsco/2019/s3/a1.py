#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
ans=""
for i in s:
    if i=="O": ans+="A"
    elif i=="A": ans+="O"
    else: ans+=i
print(ans)
