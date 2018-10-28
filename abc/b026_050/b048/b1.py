#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,x=map(int,input().split())
print((b//x)-(a//x) if a%x else (b//x)-(a//x)+1)
