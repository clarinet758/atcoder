#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d=[]
for i in range(n):
    a,b=map(str,input().split("-"))
    ah,am=int(a[:2]),(a[2:])
    bh,bm=int(b[:2]),int(b[2:])
    am-=am%5
    if bm%5: bm+=(5-bm%5)
    if bm==60:
        bh+=1
        bm=0
    d.append((3600*ah+am,3600*bh+bm))
d.sort()
ans=[[d[0][0],d[0][1]]]
for i in range(1,n):
    if d[i][0]<=ans[-1][1]:
        ans[-1][1]=max(ans[-1][1],d[i][1])
    else:
        ans.append([d[i][0],d[i][1]])
for i in ans:
    print("".join(["{0:02}".format(i[0]//3600),"{0:02}".format(i[0]%3600),"-","{0:02}".format(i[1]//3600),"{0:02}".format(i[1]%3600)]))
        
