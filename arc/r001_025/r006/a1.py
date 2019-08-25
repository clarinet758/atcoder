#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

e=[int(i) for i in input().split()]
b=int(input())
l=[int(i) for i in input().split()]
ans=0
for i in l:
    if i in e:
        ans+=1
if ans==6: print(1)
elif ans==5 and b in l: print(2)
elif ans==5: print(3)
elif ans==4: print(4)
elif ans==3: print(5)
else: print(0)
