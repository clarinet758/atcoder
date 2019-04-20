#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


a,b,c=map(int,input().split())
l=[a,b,c]
l.sort()
print("Yes" if c==l[1] else "No")
