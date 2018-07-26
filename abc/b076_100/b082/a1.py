#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a,b=map(int,input().split())
t=a+b
print(t//2+[0,1][t%2!=0])
