#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import bisect
w=20000000001
a,b,q=map(int,input().split())
s=[int(input()) for i in range(a)]
t=[int(input()) for i in range(b)]
#bisect.bisect_left

for i in range(q):
    x=int(input())
    ans=w
    tmp=x
    ls=bisect.bisect_left(s,tmp)
    lt=bisect.bisect_left(t,tmp)
    if (s[ls-1]<=tmp and t[lt-1]<=tmp): ans=min(ans,tmp-min(s[ls-1],t[lt-1]))
    if (s[ls-1]<=tmp and lt<b and t[lt]>=tmp): ans=min(ans,(tmp-s[ls-1])+(t[lt]-s[ls-1]),(t[lt]-tmp)+(t[lt]-s[ls-1]))
    if (ls<a and s[ls]>=tmp and t[lt-1]<=tmp): ans=min(ans,(tmp-t[lt-1])+(s[ls]-t[lt-1]),(s[ls]-tmp)+(s[ls]-t[lt-1]))
    if (ls<a and lt<b and s[ls]>=tmp and t[lt]>=tmp): ans=min(ans,max(s[ls],t[lt])-tmp)
    print(ans)
"""
    if (s[ls-1]<=tmp and t[lt-1]<=tmp):
        print("ll",tmp,s[ls-1],t[lt-1])
        ans=min(ans,tmp-min(s[ls-1],t[lt-1]))

    if (s[ls-1]<=tmp and lt<b and t[lt]>=tmp):
        print("lr",tmp,s[ls-1],t[lt])
        ans=min(ans,(tmp-s[ls-1])+(t[lt]-s[ls-1]))

    if (ls<a and s[ls]>=tmp and t[lt-1]<=tmp):
        print("rl",tmp,t[lt-1],s[ls])
        ans=min(ans,(tmp-t[lt-1])+(s[ls]-t[lt-1]))

    if (ls<a and lt<b and s[ls]>=tmp and t[lt]>=tmp):
        print("rr",tmp,s[ls],t[lt])
        ans=min(ans,max(s[ls],t[lt])-tmp)
"""
