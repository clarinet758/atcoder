#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class UnionFind:
    def __init__(self, size):
        self.rank=[0]*size
        self.par =[int(i) for i in range(size)]
        self.grp =size

    def find(self, x):
        if x==self.par[x]: return x

        self.par[x]=self.find(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.find(x)==self.find(y)

    def unite(self, x, y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return

        self.grp-=1
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1

    def group_num(self):
        return self.grp
t="1234567890"
n=int(input())
uf=UnionFind(100)
a=input()
b=input()
for i in range(n):
    uf.unite(ord(a[i]),ord(b[i]))

ans=chk=1
s=set()
for i in range(n):
    f=1
    if a[i] not in s:
        s.add(a[i])
        for j in t:
            if uf.same(ord(a[i]),ord(j)):
                f=0
                break
    else:
        f=0
    for j in s:
        if j!=a[i]:
            if uf.same(ord(j),ord(a[i])):
                f=0
                break
    if f and i==0: ans*=9
    elif f: ans*=10

print(ans)
