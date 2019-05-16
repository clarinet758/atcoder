#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    h,w=map(int,input().split())
    l=[]
    d=set()
    for i in range(h):
        s=list(input())
        for j in range(w):
            if s[j]=="#": d.add((i,j))
        l.append(s)
    ans=-1
    for i in range(2000):
        if len(d)==0: break
        ans+=1
        t=set()
        for j in d:
            if 0<=j[0]+1<h and l[j[0]+1][j[1]]==".":
                l[j[0]+1][j[1]]="#"
                t.add((j[0]+1,j[1]))
            if 0<=j[0]-1<h and l[j[0]-1][j[1]]==".":
                l[j[0]-1][j[1]]="#"
                t.add((j[0]-1,j[1]))
            if 0<=j[1]+1<w and l[j[0]][j[1]+1]==".":
                l[j[0]][j[1]+1]="#"
                t.add((j[0],j[1]+1))
            if 0<=j[1]-1<w and l[j[0]][j[1]-1]==".":
                l[j[0]][j[1]-1]="#"
                t.add((j[0],j[1]-1))
        d=t
    print(ans)

if __name__ == "__main__":
    sol()
