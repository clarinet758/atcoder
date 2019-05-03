#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n,x,y=map(int,input().split())
l=[int(i) for i in input().split()]
l.sort(reverse=True)
for a,i in enumerate(l):
    if a%2: y+=i
    else: x+=i
print("Takahashi" if x>y else "Aoki" if y>x else "Draw")
