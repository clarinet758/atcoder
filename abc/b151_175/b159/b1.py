#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
x=len(s)
l=s[0:(x-1)//2]
r=s[(x+3)//2-1:]
print("Yes" if s==s[::-1] and l==l[::-1] and r==r[::-1] else "No")
