#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def prime_t(t):
    i=2
    while i**2<=t:
        if t%i==0:
            return 0
        i+=1
    return 1

def prime_list(tt):
    p_list=[]
    for i in range(2,tt+1):
        if prime_t(i):
            p_list.append(i)
    return p_list

l=prime_list(201)

d={}

n=int(input())
chk=tmp=1
ans=0

for p in range(3,n+1,2):
    for i in l:
        chk=1
        while p%i==0:
            p//=i
            chk+=1
        tmp*=chk
    if tmp==8:
        ans+=1
    tmp=1
print(ans)
