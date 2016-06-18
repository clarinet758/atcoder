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

class UnionFind:
    def __init__(self, size): #class内で使ってるリストなど
        self.rank=[0]*size #高さ管理
        #self.kensu=[1]*size
        self.par=range(size)
        self.g_num=size #グループ数管理

    def find(self, x): #圧縮
        if x==self.par[x]:
            return x
        self.par[x]=self.find(self.par[x])
        return self.par[x]

    def same(self, x, y): #同じグループか判定
        return self.find(x)==self.find(y)

    def unite(self, x, y):
        x,y=self.find(x),self.find(y)
        if x==y: return #既に同じグループで閉路になる辺 何もしない

        self.g_num-=1 #違うグループ頂点を結ぶ辺なのでグループ数を1減らす
        if self.rank[x]>self.rank[y]:
            self.par[y]=x
        else:
            self.par[x]=y
            if self.rank[x]==self.rank[y]:
                self.rank[y]+=1
    def group_num(self):
        return self.g_num

#n,m=map(int,raw_input().split())
n=m=8
uf=UnionFind(n+1)

uf.unite(1,3)
print 1,uf.group_num()
uf.unite(3,2)
print 2,uf.group_num()
uf.unite(4,5)
print 3,uf.group_num()
uf.unite(6,2)
print 4,uf.group_num()
uf.unite(6,3)
print 5,uf.group_num()
#print uf.find(2)
#print uf.find(3)
#print uf.group_num()
#print uf.g_kensu(2)
#print uf.g_kensu(1)

exit()
#n=int(raw_input())
l,q=[],[]
for i in range(m):
    a,b,y=map(int,raw_input().split())
    l.append((-y,a,b))
l.sort()

Q=int(raw_input())
ans=[0]*Q
for i in range(Q):
    a,y=map(int,raw_input().split())
    q.append((-y,a,i))
q.sort()
tmp=0
for i in q:
    t=tmp
    for j in range(t,m):
        if l[j][0]<=i[0]:
            print "douro",l[j][0],'  hito',i[0]
            uf.unite(l[j][1],l[j][2])
            tmp+=1
        else:
            #print ans[i[2]],uf.group_num(i[1])
            #ans[i[2]]=uf.group_num(i[1])
            break


print ans
print uf.same(1,2)
print uf.same(0,2)
print uf.gsize(0)
print uf.gsize(2)
print uf.group_num(0)
#n,m=map(int,raw_input().split())
#l=map(int,raw_input().split())
#ans=chk=0
#end = time.clock()
#print end - start
