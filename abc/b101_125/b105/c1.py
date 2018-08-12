#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

l=[1,-2]

#for i in range(2,100):
for i in range(2,50):
    l.append(l[-1]*-2)
#print(l)
n=int(input())
for i in range(1000000):
    t=(bin(i)[2:])[::-1]
    chk=0
#    print(t)
    for j,k in enumerate(t):
#        print(k)
        if k=='1':
            chk+=l[j]
        if chk==n:
            print(t[::-1])
            exit()

#n,k=map(int,input().split())
#l=[int(i) for i in input().split()]
#ans=chk=0
#print(ans)
