#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

c1,a=map(str,input().split())
c2,b=map(str,input().split())
a=int(a)
b=int(b)
print(abs(a-b)//15 if c1==c2 else (a+b)//15)
