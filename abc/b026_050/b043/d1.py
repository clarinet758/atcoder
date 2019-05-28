#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
if len(s)==2:
    print(["-1 -1","1 2"][s[0]==s[1]])
    exit()
x=len(s)
for i in range(x-2):
    chk=[s[i],s[i+1],s[i+2]]
    chk.sort()
    if chk[0]==chk[1] or chk[1]==chk[2]:
        print(i+1,i+3)
        exit()
print("-1 -1")
