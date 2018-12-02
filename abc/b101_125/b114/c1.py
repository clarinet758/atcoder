#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=["0","3","5","7"]
s=["3","5","7"]
n=int(input())
ans=chk=0
for a in t:
    for b in t:
        for c in t:
            for d in t:
                for e in t:
                    for f in t:
                        for g in s:
                            for h in s:
                                for i in s:
                                    x=str(int(a+b+c+d+e+f+g+h+i))
                                    y=set(list(x))
                                    if ("0" not in y) and (len(y)==3) and (int(x)<=n):
                                        ans+=1
print(ans)
