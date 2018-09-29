#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
#n,k=map(int,input().split())
l=[int(i) for i in input().split()]
e,o={0:0},{0:0}
for a,i in enumerate(l):
    if a%2:
        if i in o: o[i]+=1
        else: o[i]=1
    else:
        if i in e: e[i]+=1
        else: e[i]=1
chko,chke=[0,0,0,0],[0,0,0,0]
for i in e:
    if e[i]>=chke[1]:
        chke[3]=chke[1]
        chke[2]=chke[0]
        chke[1]=e[i]
        chke[0]=i
    elif e[i]>=chke[3]:
        chke[3]=e[i]
        chke[2]=i
for i in o:
    if o[i]>=chko[1]:
        chko[3]=chko[1]
        chko[2]=chko[0]
        chko[1]=o[i]
        chko[0]=i
    elif o[i]>=chko[3]:
        chko[3]=o[i]
        chko[2]=i
#print(e,o)
#print(chko,chke)
if chko[0]!=chke[0]:
    print((n//2-chko[1])+(n//2-chke[1]))
else:
    ans=min((n//2-chko[1])+(n//2-chke[3]),(n//2-chko[3])+(n//2-chke[1]))
    print(ans)
