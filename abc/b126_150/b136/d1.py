#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#import sys
#input=sys.stdin.readline

s=input()
x=len(s)
ans=[0]*x
chk=[0,0]
f=0
for i in range(x):
    if s[i]=="R":
        chk[i%2]+=1
    if s[i]=="L":
        if i%2:
            ans[i-1]+=chk[0]
            ans[i]+=chk[1]
        else:
            ans[i]+=chk[0]
            ans[i-1]+=chk[1]

        chk=[0,0]
chk=[0,0]
for i in range(x-1,-1,-1):
    if s[i]=="L":
        chk[i%2]+=1
    if s[i]=="R":
        if i%2:
            ans[i+1]+=chk[0]
            ans[i]+=chk[1]
        else:
            ans[i]+=chk[0]
            ans[i+1]+=chk[1]
        chk=[0,0]
    
print(*ans)
