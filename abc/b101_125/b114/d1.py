#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    n=int(input())
    e=[0]*(n+1)
    for i in range(2,n+1):
        cur=i
        for j in range(2,i+1):
            while cur%j==0:
                e[j]+=1
                cur//=j


    ans=0
    for i in range(n+1):
        if e[i]>73: ans+=1


    for i in range(n):
        for j in range(i+1,n+1):
            if e[i]>23 and e[j]>1: ans+=1
            if e[i]>1 and e[j]>23: ans+=1

    for i in range(n):
        for j in range(i+1,n+1):
            if e[i]>13 and e[j]>3: ans+=1
            if e[i]>3 and e[j]>13: ans+=1

    for i in range(n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                if e[i]>3 and e[j]>3 and e[k]>1: ans+=1
                if e[i]>3 and e[j]>3 and e[k]>3: ans+=1
                if e[i]>1 and e[j]>3 and e[k]>3: ans+=1
    print(ans)

    #pdf解説のサンプルはlambda
    #def num(m):
    #    return len(list(filter(lambda x: x>=m-1,e)))
    #print(num(75)+num(25)*(num(3)-1)+num(15)*(num(5)-1)+num(5)*(num(5)-1)*(num(3)-2)//2)

if __name__=="__main__":
    sol()
