#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()
x=len(s)
ans=10**9+7
for i in range(x):
    ans=min(ans,abs(753-int(s[i:i+3])))
print(ans)
