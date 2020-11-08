#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

h=w=0
s=""
for i in range(100):
    a,b=map(int,input().split())
    if h<a:
        s+="D"*(a-h)
    elif h>a:
        s+="U"*(h-a)
    
    if w>b:
        s+="L"*(w-b)
    elif w<b:
        s+="R"*(b-w)
    s+="I"
    h=a
    w=b
print(s)
