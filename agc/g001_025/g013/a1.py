#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
l=[int(i) for i in input().split()]
ans=1
chk=-1
flg=0
for i in range(0,n):
    if chk==-1:
        chk=l[i]
    elif chk==l[i]:
        pass
    elif flg==0:
        flg=[-1,1][chk-l[i]<0]
        chk=l[i]
    elif flg==-1:
        if chk-l[i]<0:
            ans+=1
            flg=0
        chk=l[i]
    else:
        if chk-l[i]>0:
            ans+=1
            flg=0
        chk=l[i]
print(ans)
