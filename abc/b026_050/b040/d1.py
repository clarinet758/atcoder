#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
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
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

class UnionFind: #uf=UnionFind(n) で初期化？実行する。nは全体の頂点数
    def __init__(self, size):
        self.rank=[0]*size #高さ管理
        self.par=range(size) #グループの根 初期値は全て自身
        self.g_num=size #グループ数 初期値は頂点数

    def find(self, x): #圧縮
        if x==self.par[x]:
            return x
        self.par[x]=self.find(self.par[x]) #圧縮
        return self.par[x]

    def same(self, x, y): #x,yが同じグループか判定
        return self.find(x)==self.find(y)

    def unite(self, x, y):
        x,y=self.find(x),self.find(y) #findで圧縮発生することあり
        if x==y: #既に同じグループで閉路になる辺
            return
        self.g_num-=1 #違うグループ頂点を結ぶ辺なのでグループ数を1減らす
        if self.rank[x]>self.rank[y]:
            self.par[y]=x

        else:
            self.par[x]=y
            if self.rank[x]==self.rank[y]:
                self.rank[y]+=1

    def group_num(self):
        return self.g_num
    def chk_rank(self):
        return self.rank
    def chk_par(self):
        return self.par

n,m=map(int,raw_input().split())

uf=UnionFind(n+1)
#n=int(raw_input())
q=[]
for i in range(m):
    a,b,y=map(int,raw_input().split())
    q.append((-y,1,a,b))

Q=int(raw_input())
ans=[0]*(Q)
for i in range(Q):
    a,y=map(int,raw_input().split())
    q.append((-y,0,a,i))
q.sort()

for i in q:
    if i[1]==1:
        uf.unite(i[2],i[3])
    else:
        for j in range(n+1):
            uf.find(j)
        tmp=uf.chk_par()
        ans[i[3]]=tmp.count(tmp[i[2]])
for i in ans:
    print i

#print ans
#n,m=map(int,raw_input().split())
#l=map(int,raw_input().split())
#ans=chk=0
#end = time.clock()
#print end - start
