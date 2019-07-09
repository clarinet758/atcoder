#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

*e,=map(int,input().split())
b=int(input())
*l,=map(int,input().split())
ans=chk=0
for i in range(6):
    for j in range(6):
        if e[i]==l[j]:
            l[j]=-1
            break
if l.count(-1)==6:
    print(1)
elif l.count(-1)==5 and b in l:
    print(2)
elif l.count(-1)==5:
    print(3)
elif l.count(-1)==4:
    print(4)
elif l.count(-1)==3:
    print(5)
else:
    print(0)
