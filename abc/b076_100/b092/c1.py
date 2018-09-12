#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
d=[]
tmp=0
for i,j in enumerate(a):
#    print("i",tmp)
    if i==0:
        tmp+=abs(j)
        #d.append(abs(j)+abs(a[i]-a[i+1]))
        d.append(((abs(j)+abs(a[i]-a[i+1])),abs(a[i+1])))
    elif i==n-1:
        tmp+=abs(a[i-1]-a[i])+abs(j)
        d.append((abs(a[i-1]-a[i])+abs(j),abs(a[i-1])))
    else:
        f=abs(a[i]-a[i-1])
        tmp+=f
        #d.append(abs(a[i]-a[i+1])+abs(a[i]-a[i-1]))
        #print(a[i-1],a[i],a[i],a[i+1],abs(a[i-1]-a[+1]))
        #print(abs(a[i-1]-a[i]),abs(a[i]-a[i+1]),abs(a[i-1]-a[+1]))
        d.append((abs(a[i-1]-a[i])+abs(a[i]-a[i+1]),abs(a[i-1]-a[i+1])))
#print(tmp)
#print(*d)
for i in d:
    print(tmp-i[0]+i[1])
     
