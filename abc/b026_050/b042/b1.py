#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,l=map(int,input().split())
d=[input() for i in range(n)]
d.sort()
ans=""
for i in d: ans+=i
print(ans)
