#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

##WA!!!!!!!

a,b,c,d,e,f=map(int,input().split())
a*=100
b*=100
res=chk=0
ans=[]

for i in range(16):
    for j in range(16):
        for k in range(1501):
            w=(i*a)+(j*b)
            s=(k*c)
            if w==0:
                pass
            elif w+s>f:
                break
            else:
                o=(w//100)*e
                s+=((min(f-w-s,o-s)//d)*d)
                if len(ans)==0:
                    ans=[s/(w+s),w+s,s]
                elif s/(w+s)>ans[0]:
                    ans=[s/(w+s),w+s,s]
print(ans[1],ans[2])
