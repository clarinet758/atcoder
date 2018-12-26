#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def dfs(c,p):
    if p>=n-1:
        print(c)
        exit()
    if s[p+3]==".": dfs(c,p+3)
    elif s[p+2]==".": dfs(c,p+2)
    elif s[p+1]==".": dfs(c,p+1)
    else: dfs(c+1,p+3)
n=int(input())
s=input()+"...."
ans=chk=0
ans=dfs(0,0)
