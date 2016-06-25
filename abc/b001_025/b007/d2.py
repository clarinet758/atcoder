#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
#n=int(raw_input())
a,b=map(int,raw_input().split())
ans=0

def solve(v):
#vに代入されるB, A-1が0以下なら0を返す Aが3の場合はA-1が0以下に
#ならないのでこの判定をスルーされても0を返すので必要か不明??
    if v<=0:
        return 0
    if v>=1000000000000000000:
        v-=1
    vv=ld=1
    ret=0
#e,g, vが12345であったなら12345を超えないように10をかけ続けると10000になる
#

    while vv*10<=v:
        vv*=10
        ld*=8

    for i in range(v/vv):
        ret+=vv
        if  i!=4 and i!=9:
            ret-=ld
    if v/vv==4 or v/vv==9:
        return ret+(v-(v/vv)*vv+1)
    else:
        return ret+solve(v-(v/vv)*vv)
print solve(b)-solve(a-1)
#end = time.clock()
#print end - start
