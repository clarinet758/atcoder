#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def ns(X, n):
    if (int(X/n)):
        return ns(int(X/n), n)+str(X%n)
    return str(X%n)

n,a,b,c=map(int,input().split())
t=[a,b,c]
l=[]
ans=-1
for i in range(n):
    l.append(int(input()))

for i in range(4**n):
    tmp=ns(i,4)
    tmp="0"*(n-len(tmp))+tmp
    h=[0]*3
    p=0
    for j in range(n):
        if tmp[j]=="1":
            if h[0]!=0: p+=10
            h[0]+=l[j]

        elif tmp[j]=="2":
            if h[1]!=0: p+=10
            h[1]+=l[j]

        elif tmp[j]=="3":
            if h[2]!=0: p+=10
            h[2]+=l[j]

    if 0 in h:continue
    for k in range(3):
        p+=abs(h[k]-t[k])
    if ans==-1: ans=p
    else: ans=min(ans,p)
print(ans)

        
    
"""    
for i in range(n):
    x=int(input())
    if x in t: t.remove(x)
    else: l.append(x)]
"""

