#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#n=int(input())
def sol():
    n,m=map(int,input().split())
    k=[]
    for i in range(m):
        l=[int(i) for i in input().split()]
        k.append([l[j]-1 for j in range(1,l[0]+1)])
    p=[int(i) for i in input().split()]
    ans=0
    #for i in range(2**10):
    for i in range(2**n):
        s=bin(i)[2:]
        s="0"*(n-len(s))+s
        s=s[::-1]
        for a,j in enumerate(k):
            chk=f=0
            for x in j:
                if s[x]=="1":
                    chk+=1
            if chk%2!=p[a]:
                f=1
                break
        if f==0:
            ans+=1
    print(ans)

if __name__=="__main__":
    sol()
