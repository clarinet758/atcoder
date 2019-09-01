#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b=map(int,input().split())
ans=0
cnt=1
while cnt<b:
    cnt-=1
    cnt+=a
    ans+=1
print(ans)
