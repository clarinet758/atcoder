#!/usr/bin/env python
# -*- coding: UTF-8 -*-

mod=1777777777
def sol(pos, use, nokori, n):
    #残った人数の確認
    if pos==n:
        if nokori==0: return 1
        else: return 0

    ret=0
    #pos番目の人が誰の手紙を受け取ったか調べる
    for i in range(n):
        if use[i]: continue
        #手紙の使用フラグ
        use[i]=1

        #残りの間違える個数を更新
        tmp=nokori
        if i!=pos:
            tmp-=1
        ret+=sol(pos+1, use, tmp, n)
        use[i]=0
    return ret



n,k=map(int,raw_input().split())
use=[0]*n

if n>100: print 0
else: print sol(0, use, k, n)
