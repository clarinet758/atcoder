#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=input()
s=""
for i in n:
    if i=="1" or i=="9":
        s+=["1","9"][i!="9"]
    else:
        s+=i
print(s)
