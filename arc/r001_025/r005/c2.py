#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()


##外周全てに#を3つずつ付け足すために迷路はhw両方向に6ずつ大きくなる
##今回は許容される壁破壊、#への立ち入りが2回なので外周に踏み込んだら
##戻ってこれないことが保証される

h,w=[int(x)+2 for x in raw_input().split()] #迷路の大きさ行・列
##外周外周外周外周
##      塀
##3回以上許容されると外周外を歩いて戻ってきてしまう
##ことが可能なので何か強制終了条件で管理かな？
##外周に*を配置と強制死亡にしたバージョン
#cw=[list(raw_input()) for _ in range(h)]
cw=['*'*w]+['*'+raw_input()+'*' for _ in range(h-2)]+['*'*w] #迷路
t=[[9]*w for i in range(h)] #その座標にいる時に壁破壊が何回かカウンター
d=[[],[],[]] #壁の破壊回数i回の地点
ans=chk=0
##問題から入力でスタート、ゴールの座標が与えられないので自分で探す
##まぁ与えられてても3ずつずれるのでその分は要修正ですけど
for i in range(h):
    if chk==2:
        break
    for j in range(w):
        if cw[i][j]=='s':
            sh,sw=i,j
            chk+=1
        elif cw[i][j]=='g':
            gh,gw=i,j
            chk+=1
        if chk==2:
            break
##発見したスタート地点の座標を0にして、探索qリストに座標を入れる
t[sh][sw]=0
#d[0]+=[(sh,sw)]
d[0]+=[(sw,sh)]

for i in d:
    while len(i)>0:
        x,y=i.pop()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            mx,my=x+dx,y+dy #移動先の座標が決まる
##移動先が'#'なら1加算、そうでなければ同じカウントのまま
            if cw[my][mx]=='#':
                dt=t[y][x]+1
            elif cw[my][mx]=='*':
                dt=t[y][x]+3
            else:
                dt=t[y][x]
            if dt<=2 and dt<t[my][mx]:
                t[my][mx]=dt
                d[dt]+=[(mx,my)]
for i in range(h):
    for j in range(w):
        if cw[i][j]=='g':
            print 'YES' if t[y][x]<=2 else 'NO'
#end = time.clock()
#print end - start
