#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
#162258 のkusanoさんのパクリです。
r,c=map(int,raw_input().split()) #迷路の大きさ

##sy,sx,gy,gxをtype()でみてみたけど,-1されたint型だった
##リストが0-basedで、座標は1-basedなことを他の方法で調整するなら
##lambdaは必須ではないと思う
sy,sx=map(lambda x: int(x)-1, raw_input().split()) #スタート座標
gy,gx=map(lambda x: int(x)-1, raw_input().split()) #ゴール座標
cw=[raw_input() for _ in range(r)] #r行c列地図

t=[[-1]*c for y in range(r)] #r*cの-1を並べたリスト。現在地や通過済の管理用。

ans=chk=0
t[sy][sx]=0 #スタート地点を0にする
q=[(sx,sy)]

while t[gy][gx]==-1: #ゴール地点座標が-1(まだゴールに到達できていない)なら繰返し
    fx,fy=q.pop(0) #fxにq[0][0],fyにq[0][1]がint型で入る
    for d in range(4): #4方向確認のため
##現在地の座標に(-1,0),(1,0),(0,-1),(0,1)を加算することで
##移動先の座標を決める
        tx=fx+[-1,1,0,0][d]
        ty=fy+[0,0,-1,1][d]
        if cw[ty][tx]=='.' and t[ty][tx]==-1: #移動可能な.で未通過の-1なら処理
            t[ty][tx]=t[fy][fx]+1 #現在地の歩数+1を移動先座標に上書き
##新しい現在地と言っても幅優先なのでアレ
            q+=[(tx,ty)]#新しい現在地をqに入れる

print t[gy][gx]
#end = time.clock()
#print end - start
