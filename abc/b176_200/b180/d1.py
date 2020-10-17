#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

x,y,a,b=map(int,input().split())
ans=0
while 1:
    if x*a<=x+b and x*a<y:
        x*=a
        ans+=1
    else:
        ans+=(y-x-1)//b
        break
print(ans)
