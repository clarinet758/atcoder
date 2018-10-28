#!/usr/bin/env python3

n=int(input())

x,y=map(int, input().split())
for i in range(n-1):
    t,a=map(int, input().split())
    if (x<=t and y<=a):
        x=t
        y=a
    else:
        tmp=0
        k=max(x//t,y//a)
        tk=t*k
        ak=a*k
        while 1:
            if x<=tk+(tmp*t) and y<=ak+(tmp*a):
                x=tk+(tmp*t)
                y=ak+(tmp*a)
                break
            tmp+=1
print(x+y)
