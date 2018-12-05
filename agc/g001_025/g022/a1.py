#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()
l=[0]*26
for i in s:
    l[ord(i)-ord("a")]=1
if len(s)<26:
    for i in range(26):
        if l[i]==0:
            print(s+chr(i+ord("a")))
            exit()
else:
    for i in range(26):
        l[ord(s[-i-1])-ord("a")]=0
        for j in range(26):
            if l[j]==0 and ord(s[-i-1])-ord("a")<j:
                print(s[:-i-1]+chr(j+ord("a")))
                exit()
print(-1)
