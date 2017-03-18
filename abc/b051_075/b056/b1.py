#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

w,a,b=map(int,input().split())
print(max(max(a,b)-min(a,b)-w,0))
