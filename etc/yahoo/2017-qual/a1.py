#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

s=list(input())
chk=list('yahoo')
s.sort()
chk.sort()
ans=[s[i]==chk[i] for i in range(5)]
print('YES' if all(ans) else 'NO')
