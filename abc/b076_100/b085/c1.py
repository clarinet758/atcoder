#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def chk(l):
    return l[0]*10+l[1]*5+l[2]

n,y=[int(x) for x in input().split()]
y//=1000
n-=y%5
ans=[0,n,y%5]
t=n*2
while t>=0:
    t-=1
    if y==chk(ans):
        break
    elif y>chk(ans) and ans[1]>0:
        ans[1]-=1
        ans[0]+=1
    elif y<chk(ans) and ans[1]>4:
        ans[1]-=5
        ans[2]+=5
    elif y>chk(ans) and ans[2]>0:
        ans[2]-=1
        ans[0]+=1
    elif y<chk(ans) and ans[0]>4:
        ans[0]-=5
        ans[2]+=5
        
if y==chk(ans):
    print(*ans)
else:
    print("-1 -1 -1")

