#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#from https://atcoder.jp/contests/abc137/submissions/6808061
import heapq
import sys
input=sys.stdin.readline

def sol():
    n,m=map(int,input().split())
    d=[]
    for i in range(n):
        a,b=map(int,input().split())
        if a<=m: d.append((a,b))
    d.sort(reverse=True)
    q=[]
    ans=0
    for i in range(1,m+1):
        while d and d[-1][0]<=i:
            a,b=d.pop()
            heapq.heappush(q,-b)
        if q:
            ans += -heapq.heappop(q)
    print(ans)
    
if __name__=="__main__":
    sol()

"""
 
def sol():
    n,m=map(int,input().split())
    d=[]
    ans=[0]*(m+1)
    t=0
    ans[0]=1
    y=m
    for i in range(n):
        a,b=map(int,input().split())
        if a<=m: heapq.heappush(d,(-b,-a))
    while len(d):
        bb,aa=heapq.heappop(d)
        aa*=-1
        if 0 not in ans:
            break
        if max(ans.index(0),aa)==y:
            ans[y]=1
            t+=bb
            y-=1
        else:
            for j in range(max(ans.index(0),aa),y+1):
                if ans[j]==0:
                    ans[j]=1
                    t+=bb
                    break
 
    print(-1*t)
 
if __name__=="__main__":
    sol()
"""
