#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import re
import math
import itertools
import collections
import bisect
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def fib(n): return [(seq.append(seq[i-2] + seq[i-1]), seq[i-2])[1] for seq in [[0, 1]] for i in range(2, n)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
def pscl(num,l=[1]):
    for i in range(num):
        l = map(lambda x,y:x+y,[0]+l,l+[0])
    return l

class UnionFind:
    def __init__(self, size):
        self.rank=[0]*size
        self.par =range(size)
        self.grp =size

    def find(self, x):
        if x==self.par[x]: return x

        self.par[x]=self.find(self.par[x])
        return self.par[x]

    def same(self, x, y): #2つの頂点が同じグループであるかを判定する
        return self.find(x)==self.find(y)

    def unite(self, x, y): #辺で接続されている2つの頂点を投げて統合する
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
    def ra(self):
        return self.rank

class UnionFind2:
    def __init__(self, size):
        self.rank=[0]*size
        self.par =range(size)
        self.grp =size

    def find(self, x):
        if x==self.par[x]: return x

        self.par[x]=self.find(self.par[x])
        return self.par[x]

    def same(self, x, y): #2つの頂点が同じグループであるかを判定する
        return self.find(x)==self.find(y)

    def unite(self, x, y): #辺で接続されている2つの頂点を投げて統合する
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


n,k,l=map(int,raw_input().split())
uf=UnionFind(n)
uf2=UnionFind2(n)
q1,q2=[],[]
ans=[0]*n
for i in range(k):
    a,b=map(int,raw_input().split())
    uf.unite(a-1,b-1)
    q1.append((a-1,b-1))
    ans[a-1]=1
    ans[b-1]=1

for i in range(l):
    a,b=map(int,raw_input().split())
    uf2.unite(a-1,b-1)
    if ans[a-1]==0: ans[a-1]=1
    if ans[b-1]==0: ans[b-1]=1
    if uf.same(a-1,b-1):
        ans[a-1]=2
        ans[b-1]=2

for i in q1:
    if uf2.same(i[0],i[1]):
        ans[i[0]]=2
        ans[i[1]]=2
print ' '.join(map(str,ans))
