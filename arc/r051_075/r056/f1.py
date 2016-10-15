#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#from guppy import hpy
import heapq
from copy import deepcopy
n,m=map(int, raw_input().split())
boad=[]

class Dijkstra:
    def __init__(self):
        pass
nr=n
while nr:
    nr-=1
    boad.append([])
rm=m
while rm:
    rm-=1
    a,b,c=map(int, raw_input().split())
    a,b=a-1,b-1
#移動先 コスト
    boad[a].append((b,c))
    boad[b].append((a,c))

#コスト 現在地 ルート
ans=[[0,0,[1]]]
memo=[-1]*n
memo[0]=0

while len(ans):
    q=heapq.heappop(ans)
#   q: [0,0,[1]]
#最安コストのものを取り出してゴールにいれば出力して終わる
    if q[1]==n-1:
        print ' '.join(map(str,q[2]))
        exit()

#現在地から移動先を探す
    for x in boad[q[1]]:
        k=deepcopy(q)
        c=k[0]+x[1]
#コスト比較は現在k[0]+移動コストx[1] と 移動先memo[x[0]]
        if memo[x[0]]==-1 or (memo[x[0]]!=-1 and memo[x[0]]>k[0]+x[1]):
            k[0]=c
            memo[x[0]]=c
            k[1]=x[0]
            k[2].append(x[0]+1)
            heapq.heappush(ans,k)
print -1

#hp = hpy()
#print hp.heap()
