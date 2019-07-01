#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
t=len(s)
ans=0
for a,i in enumerate(s):
    if i=="U":
        ans+=t-a-1
        ans+=a*2
    else:
        ans+=(t-a-1)*2
        ans+=a
print(ans)
