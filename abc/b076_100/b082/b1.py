#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()
t=input()
a,b=[],[]
for i in s:
    a.append(ord(i))
for i in t:
    b.append(ord(i))
a.sort()
b.sort()
b=b[::-1]

for i in range(min(len(a),len(b))):
    if a[i]>b[i]:
        print("No")
        exit()
    elif a[i]<b[i]:
        print("Yes")
        exit()
print("Yes" if len(a)<len(b) else "No")
