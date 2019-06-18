#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
a.sort()
x=a[-1]
ans=[x,0]
for i in a:
    if x>i and abs(x//2-i)<abs(x//2-ans[1]):
        ans[1]=i
    if x>i and x%2 and abs((x+1)//2-i)<abs((x+1)//2-ans[1]):
        ans[1]=i

print(ans[0],ans[1])

