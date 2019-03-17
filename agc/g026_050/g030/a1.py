#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,c=map(int,input().split())
print(b+[c,a+b+1][a+b<c])
