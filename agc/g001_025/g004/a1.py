#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
l=[int(i) for i in input().split()]
ans=max(l)**3
for i in range(3):
    t=l[(0+i)%3]*l[(1+i)%3]
    ans=min(ans,t*((l[(2+i)%3]+1)//2)-t*(l[(2+i)%3]//2))
print(ans)
