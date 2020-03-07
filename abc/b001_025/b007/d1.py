#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def cnt(x):
    sq=[4,9]
    l=[int(i) for i in "0"+str(x)]
    # [0]=n  [1]<n
    dp=[[[0]*2,[0]*2] for _ in "xx"]
    dp[0][0][0]=1
    for i in range(1,len(l)):
        j=l[i]
        if dp[i%2-1][0][1] or j in sq:
            dp[i%2][0][1]=1
        else:
            dp[i%2][0][0]=1

        if dp[i%2-1][0][0]:
            for k in range(j):
                if k==4: dp[i%2][1][1]+=1
                else: dp[i%2][1][0]+=1
        else:
            dp[i%2][1][1]+=j

        if dp[i%2-1][1][1]:
            dp[i%2][1][1]+=dp[i%2-1][1][1]*10

        if dp[i%2-1][1][0]:
            dp[i%2][1][0]+=dp[i%2-1][1][0]*8
            dp[i%2][1][1]+=dp[i%2-1][1][0]*2
                    

        for k in range(4):
            aa,bb=k//2,k%2
            dp[i%2-1][aa][bb]=0
    r=0
    for k in range(4):
        aa,bb=k//2,k%2
        r+=dp[aa][bb][-1]
    
    #for k in dp:
    #    print(k)
    return r

a,b=map(int,input().split())
a-=1
print(cnt(b)-cnt(a))
