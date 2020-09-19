#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
for i in range(n):
    s=input()
    t=len(s)
    s+="######"
    ans=[100]*2
    for i in range(t):
        if ans[0]==100 and s[i]=="o" and s[i+1]=="k" and s[i+2]=="y" and s[i+3]=="o":
            ans[0]=i
        if s[i]=="e" and s[i+1]=="c" and s[i+2]=="h":
            ans[1]=i
    if ans[0]<ans[1]<100:
        print("Yes")
    else:
        print("No")
