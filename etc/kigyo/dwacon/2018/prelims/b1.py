#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

ans=0
s=input()
t=s
while len(t):
    d,p="",""
    
    for a,i in enumerate(t):
        if d=="" and i=="2": d=i
        elif d=="2" and i=="5": d=""
        else: p+=i
    if p+d==t:
        print(-1)
        exit()
    t=p+d
    ans+=1
print(ans)
