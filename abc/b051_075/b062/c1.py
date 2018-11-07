#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

h,w=map(int,input().split())
ans=h*w
for x,y in ((h,w),(w,h)):
    x1=x//3
    x2=(x+2)//3
    y2=(y+1)//2
    ans=min(ans,abs(y*x2-y*x1))
    t=(y*x1,y2*(x-x1),(y-y2)*(x-x1))
    ans=min(ans,max(t)-min(t))
    t=(y*x2,y2*(x-x2),(y-y2)*(x-x2))
    ans=min(ans,max(t)-min(t))
print(ans)
