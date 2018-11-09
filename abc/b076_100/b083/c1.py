#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

x,y=map(int,input().split())
ans=1
while 1:
    x*=2
    if x>y: break
    ans+=1
print(ans)
