#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())*3
l=[int(i) for i in input().split()]
l.sort()
ans=chk=0
for i in range(-2,(n//3*2)*-1-1,-2):
    ans+=l[i]
print(ans)
