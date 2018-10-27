#!/usr/bin/env python3

s=input()

ans=tmp=0
t=len(s)

for i in range(1<<(t-1)):
#    print(i)
    tmp=int(s[0])
    for j in range(t-1):
        if (i & (1<<j)):
            tmp*=10
            tmp+=int(s[j+1])
        else:
            ans+=tmp
            tmp=int(s[j+1])
    ans+=tmp
print(ans)
