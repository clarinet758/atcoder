#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=int(input())
v=1000000000
x=(v-s%v)%v
y=(s+x)//v
print(0,0,v,1,x,y)
