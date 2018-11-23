#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,w=map(int,input().split())
d={}
p=0
ans=[0,0]
u=[[] for i in range(4)]
for i in range(n):
    a,b=map(int,input().split())
    if a in d: d[a].append(b)
    else:d[a]=[0,b]
    p=max(p,a)
for i in range(4):
    if p-i in d: d[p-i].sort()
    else: d[p-i]=[0]

for x in range(4):
    if len(d[p-x])*(p-x)+ans[0]<=w:
        ans[0]+=len(d[p-x])*(p-x)
        ans[1]+=sum(d[p-x])
        u[x]=[o for o in d[p-x]]
        d[p-x]=[0]
    else:
        for i in range(-1,-1-len(d[p-x]),-1):
            if p+ans[0]-x<=w:
                ans[0]+=p-x
                ans[1]+=d[p-x][-1]
                u[x].append(d[p-x].pop())
            else:
                break
#u[-1].sort(reverse=True)
for i in range(3):
    while len(u[i]):
        if u[i][-1]<d[p-i-1][-1]:
            ans[0]-=1
            ans[1]+=d[p-i-1][-1]
            u[i].pop()
            u[i+1].append(d[p-i-1].pop())
        elif (p-i-2 in d) and u[i][-1]<d[p-i-2][-1]:
            ans[0]-=2
            ans[1]+=d[p-i-2][-1]
            u[i].pop()
            u[i+2].append(d[p-i-2].pop())
        elif (p-i-3 in d) and u[i][-1]<d[p-i-3][-1]:
            ans[0]-=3
            ans[1]+=d[p-i-3][-1]
            u[i].pop()
            u[i+3].append(d[p-i-3].pop())
        elif len(d[p-i-1])>1 and w>=ans[0]+(p-i-1)+(p-i-1) and u[i][-1]<d[p-i-1][-1]+d[p-i-1][-1]:
            ans[0]-=p-i
            ans[0]+=(p-i-1)+(p-i-1)
            ans[1]+=d[p-i-1][-1]
            ans[1]+=d[p-i-1][-2]
            u[i].pop()
            u[i+1].append(d[p-i-1].pop())
            u[i+1].append(d[p-i-1].pop())
        elif (p-i-2 in d) and d[p-i-2][-1]>0 and w>=ans[0]+(p-i-1)+(p-i-2) and u[i][-1]<d[p-i-1][-1]+d[p-i-2][-1]:
            ans[0]-=p-i
            ans[0]+=(p-i-1)+(p-i-2)
            ans[1]+=d[p-i-1][-1]
            ans[1]+=d[p-i-2][-1]
            u[i].pop()
            u[i+1].append(d[p-i-1].pop())
            u[i+2].append(d[p-i-2].pop())
        elif (p-i-2 in d) and len(d[p-i-2])>1 and d[p-i-2][-2]>0 and w>=ans[0]+((p-i-2)*2) and u[i][-1]<d[p-i-2][-1]+d[p-i-2][-2]:
            ans[0]-=p-i
            ans[0]+=(p-i-2)*2
            ans[1]+=d[p-i-2][-1]
            ans[1]+=d[p-i-2][-2]
            u[i].pop()
            u[i+2].append(d[p-i-2].pop())
            u[i+2].append(d[p-i-2].pop())
        elif (p-i-3 in d) and d[p-i-3][-1]>0 and w>=ans[0]+(p-i-1)+(p-i-3) and u[i][-1]<d[p-i-1][-1]+d[p-i-3][-1]:
            ans[0]-=p-i
            ans[0]+=(p-i-1)+(p-i-3)
            ans[1]+=d[p-i-1][-1]
            ans[1]+=d[p-i-3][-1]
            u[i].pop()
            u[i+1].append(d[p-i-1].pop())
            u[i+3].append(d[p-i-3].pop())
        else:
            break
print(ans[1])
