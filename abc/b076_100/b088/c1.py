#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
print("Yes" if a[0]-b[0]==a[1]-b[1]==a[2]-b[2] and a[0]-c[0]==a[1]-c[1]==a[2]-c[2] else "No")
