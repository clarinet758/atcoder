#!/usr/bin/env python3

n,m=map(int, input().split())
x,y=map(int, input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
a=a[::-1]
b=b[::-1]

ans=[0]*3
while 1:
    if ans[2]==0: t=a.pop()
    else: t=b.pop()

    if ans[2]==0 and t>=ans[1]:
        ans[1]=t+x
        ans[2]=1
    elif ans[2]==1 and t>=ans[1]:
        ans[1]=t+y
        ans[2]=0
        ans[0]+=1
    if (ans[2]==0 and len(a)==0) or (ans[2]==1 and len(b)==0):
        break
print(ans[0])
