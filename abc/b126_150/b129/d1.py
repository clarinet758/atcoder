#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    h,w=map(int,input().split())
    l=[]
    x=[[0]*w for i in range(h)]
    y=[[0]*w for i in range(h)]
    for i in range(h):
        s=input()
        l.append(s)
    for i in range(h):
        for j in range(w):
            if j==0 and l[i][j]==".":
                x[i][j]=1
            elif l[i][j]==".":
                x[i][j]=x[i][j-1]+1
    for i in range(h):
        for j in range(1,w):
            t=-1*(j+1)
            if l[i][t]==".":
                x[i][t]=max(x[i][t],x[i][t+1])

    for i in range(w):
        for j in range(h):
            if j==0 and l[j][i]==".":
                y[j][i]=1
            elif l[j][i]==".":
                y[j][i]=y[j-1][i]+1
    for i in range(w):
        for j in range(1,h):
            t=-1*(j+1)
            if l[t][i]==".":
                y[t][i]=max(y[t][i],y[t+1][i])
    ans=chk=0
    for i in range(h):
        for j in range(w):
            ans=max(ans,x[i][j]+y[i][j]-1)
    print(ans)

if __name__=="__main__":
    sol()
            
