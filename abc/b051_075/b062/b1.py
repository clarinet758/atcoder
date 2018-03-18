#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

h,w=map(int,input().split())
for i in range(h+2):
    if i==0 or i==h+1:
        print("#"*w+"##")
    else:
        a=input()
        print("#"+a+"#")
