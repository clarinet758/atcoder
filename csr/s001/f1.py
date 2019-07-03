#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

input()
a=[int(i) for i in input().split()]
ans=chk=0
for i in a:
    ans+=i>chk
    chk=max(i,chk)
print(ans)
