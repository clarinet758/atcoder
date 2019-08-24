#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

h,w=map(int,input().split())
ans=h*w
if h==w==2:
    print(1)
    exit()
if h>2:
    t=[h//3*w,(h-(h//3))//2*w,(h-(h//3)+1)//2*w]
    t.sort()
    ans=min(ans,t[2]-t[0])
if w>2:
    t=[w//3*h,(w-(w//3))//2*h,(w-(w//3)+1)//2*h]
    t.sort()
    ans=min(ans,t[2]-t[0])
a,b=h,w
for i in range(max(1,a//3-1),min(a//2+1,a-1)):
    t=[i*b,(a-i)*(b//2),(a-i)*((b+1)//2)]
    t.sort()
    ans=min(ans,t[2]-t[0])
a,b=w,h
for i in range(max(1,a//3-1),min(a//2+1,a-1)):
    t=[i*b,(a-i)*(b//2),(a-i)*((b+1)//2)]
    t.sort()
    ans=min(ans,t[2]-t[0])
print(ans)
