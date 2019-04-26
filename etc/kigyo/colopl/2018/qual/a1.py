#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


a,b=map(int,input().split())
s=input()
print(["NO","YES"][a<=len(s)<=b])
