#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
WA!!!!
"""
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
chk=a.index(1)
l=chk+k-2
r=n-(chk+1)+k-2
t1=(k%(k-1))-(l%(k-1))
t2=(k%(k-1))-(r%(k-1))
print(min(l//(k-1)+r//(k-1),((l-t2)//(k-1)+r//(k-1)), (l//(k-1)+(r-t1)//(k-1))))
#print(t1,t2)
#print((l//(k-1),r//(k-1),((l-t2)//(k-1),r//(k-1)), (l//(k-1),(r-t1)//(k-1))))
