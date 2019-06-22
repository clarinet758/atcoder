#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d=[]
for i in range(n):
    a,b=map(int,input().split())
    d.append((b,a))
d.sort()
chk=0
for i in d:
    chk+=i[1]
    if chk>i[0]:
        print("No")
        exit()
print("Yes")
