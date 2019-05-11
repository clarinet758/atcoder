#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=0
d={"a":0,"b":0,"w":0}
for i in range(n):
    s=input()
    if s[0]=="B" and s[-1]=="A": d["w"]+=1
    elif s[0]=="B" : d["b"]+=1
    elif s[-1]=="A" : d["a"]+=1
    ans+=s.count("AB")
if d["a"]==0 and d["w"]>0:
    d["a"]=1
    d["w"]-=1
if d["w"]>0:
    ans+=d["w"]
    d["w"]=0
    d["a"]-=1
    if d["b"]>0:
        ans+=1
        d["b"]-=1
ans+=max(0,min(d["a"],d["b"]))
print(ans)
