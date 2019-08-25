#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

xy=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
h,w=map(int,input().split())
l=[list(input()) for i in range(h)]
ans=[0]*3
for p in range(h*w):
    i=p//w
    j=p%w
    if l[i][j]=="o":
        t={(i,j)}
        l[i][j]="x"
        cnt=1
        nin=nax=j
        while len(t):
            a,b=t.pop()
            for x,y in xy:
                x,y=x+a,y+b
                if l[x][y]=="o":
                    cnt+=1
                    l[x][y]="x"
                    t.add((x,y))
                    nin,nax=min(nin,y),max(nax,y)
        cnt//=((nax-nin+1)//5)**2
        if cnt==12: ans[0]+=1 
        elif cnt==16: ans[1]+=1
        elif cnt==11: ans[2]+=1
        else: ans[4]+=1 #RE
print(*ans)
