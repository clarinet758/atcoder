#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

x,y=map(int,input().split())
a=[4,6,9,11]
if x==2 or y==2 or (x in a and y not in a) or (x not in a and y in a):
    print("No")
else:
    print("Yes")
