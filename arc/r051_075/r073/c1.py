#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,t=map(int,input().split())
a=[int(i) for i in input().split()]
ans=chk=0
for i in a:
    if chk<=i:
        ans=ans+t
        chk=i+t
    else:
        ans=ans+((i+t)-chk)
        chk=chk+((i+t)-chk)

print(ans)
