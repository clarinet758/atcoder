#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,k=map(int,input().split())
ans=[a,b]
for i in range(k):
    if i%2:
        ans[0]+=ans[1]//2
        ans[1]//=2
    else:
        ans[1]+=ans[0]//2
        ans[0]//=2
print(*ans)
