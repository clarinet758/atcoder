#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()

t=len(s)

A=ord("A")
Z=ord("Z")
f=0
for a,i in enumerate(s):
    if a==0:
        if i!="A":
            print("WA")
            exit()
    elif a==1:
        if A<=ord(i)<=Z:
            print("WA")
            exit()
    elif a<t-1:
        if (i=="C" and f==1) or (A<=ord(i)<=Z and i!="C"):
            print("WA")
            exit()
        elif i=="C" and f==0:
            f=1
    else:
        if A<=ord(i)<=Z:
            print("WA")
            exit()
print("AC" if f==1 else "WA")
       

