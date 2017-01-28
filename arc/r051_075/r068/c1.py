#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
if n<7:
    print(1)
elif n<12:
    print(2)
else:
    ans=n//11*2
    print(ans+[1,2][n%11>6] if n%11 else ans)

exit()

if n>=12:
    ans=(n//11)*2
    print(ans+[1,2][n%11>6])
elif 11>=n>6:
    print(2)
else:
    print(1)

