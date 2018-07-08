#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
x,a,b=map(int,input().split())
print("A" if abs(x-a)<=abs(x-b) else "B")
