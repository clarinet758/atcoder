#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()[::-1]
x=list(s)
ans=""
for i in range(len(s)-1):
    if x[i]=="A" and x[i+1]=="W":
        ans+="C"
        x[i+1]="A"
    else:
        ans+=x[i]
ans+=x[-1]        
print(ans[::-1])
