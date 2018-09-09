#!/usr/bin/env python3

h,w=map(int,input().split())
l=[]
for i in range(h):
    l.append(list(map(int,input().split())))
#print(*l)
ans=[]
for i in range(h):
    for j in range(w):
        i2,j2=i,j
        if i2%2: j2=w-(j+1)
#        print(l[i2][j2],i+1,j2+1)
        o,p=i2,j2
        if l[i2][j2]%2:
            if i2%2==0 and j2<w-1: p+=1
            elif i2%2==0 and i2<h-1: o+=1
            elif i2%2 and j2>0: p-=1
            elif i2%2 and i2<h-1: o+=1
            if i2!=o or j2!=p:
                l[i2][j2]-=1
                l[o][p]+=1
                ans.append((i2+1,j2+1,o+1,p+1))

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])

