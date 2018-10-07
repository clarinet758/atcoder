#!/usr/bin/env python3

n=int(input())

d=[0,0,0]
for i in range(n):
    t,x,y=map(int,input().split())
    tmp=abs(x-d[1])+abs(y-d[2])
    print(tmp)
    if t-d[0]>=tmp and ((t-d[0])-tmp)%2==0:
        d=[t,x,y]
    else:
        print("No")
        exit()
print("Yes")

