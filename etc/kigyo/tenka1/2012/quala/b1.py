#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

c=input()
ans=""
for a,i in enumerate(c):
    if i==" " and c[a-1]!=" ":
        ans+=","
    elif i!=" ":
        ans+=i
print(ans)
