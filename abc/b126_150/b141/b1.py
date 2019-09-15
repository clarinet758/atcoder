#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


s=input()
ans=1
for a,i in enumerate(s):
    if (a%2 and i=="R") or (a%2==0 and i=="L"):
        ans=0
print(["No","Yes"][ans])
