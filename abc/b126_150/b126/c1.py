#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    n,k=map(int,input().split())
    ans=0
    for i in range(1,n+1):
        f=0
        while 1:
            if i>=k:
                break
            i*=2
            f+=1
        ans+=(1/n)*(1/(2**f))
    print(ans)

if __name__=="__main__":
    sol()
