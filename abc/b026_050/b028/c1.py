#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import itertools

l=map(int,raw_input().split())
ans=set([])
for i in itertools.permutations(l,3):
    ans.add(sum(i))
ans=list(ans)
ans.sort()
print ans[-3]
