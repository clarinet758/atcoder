#!/usr/bin/env python3

x1,y1,x2,y2=map(int,input().split())
if x1<x2: a,b,c,d=x1,y1,x2,y2
else: a,b,c,d=x2,y2,x1,y1

t=abs(a-c)
p=b/(b+d)*t
print(a+p)
