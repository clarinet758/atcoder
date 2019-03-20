#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


a,b=map(int,input().split())
p=[int(i) for i in input().split()]
q=[int(i) for i in input().split()]
ans=[["x","x","x","x"], [" x","x","x"], ["  x","x"], ["   x"]]
d={0:[0,3],1:[3,0],2:[2,0],3:[2,1],4:[1,0],5:[1,1],6:[1,2],7:[0,0],8:[0,1],9:[0,2]}
for i in p:
    tmp=ans[d[i][0]][d[i][1]]
    tmp=tmp.replace("x",".")
    ans[d[i][0]][d[i][1]]=tmp
for i in q:
    tmp=ans[d[i][0]][d[i][1]]
    tmp=tmp.replace("x","o")
    ans[d[i][0]][d[i][1]]=tmp
for i in ans:
    print(*i)
