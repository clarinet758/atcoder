#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,c,d=map(int,input().split())
print("Yes" if abs(a-c)<=d or (abs(a-b)<=d and abs(b-c)<=d) else "No")
