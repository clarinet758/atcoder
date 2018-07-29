#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a,b,c,d=map(int,input().split())
print("Right" if c+d>a+b else "Left" if c+d<a+b else "Balanced")
