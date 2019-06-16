#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#n=int(input())
def sol():
    n,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    d=[0]
    for i in range(n):
        if i==0:
            d.append(a[i])
        else:
            d.append(d[-1]+a[i])
    #print(d)
    p,q=0,0
    ans=0
    while p<n:
        while q<n+1:
            #print(d[q]-d[p])
            if d[q]-d[p]>=k:
                ans+=(n-q+1)
                break
            q+=1
        p+=1
    print(ans)

if __name__=="__main__":
    sol()
