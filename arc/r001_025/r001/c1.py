#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#8個くらいWA出る

def chk(b,y,x):
    for i in range(1,8):
        #縦チェック
        if b[(y+i)%8][x]=='Q':
            return 0
        #横チェック
        if b[y][(x+i)%8]=='Q':
            return 0
        #右下チェック
        if 0<=y+i<8 and 0<=x+i<8 and b[y+i][x+i]=='Q':
            return 0
        #左上チェック
        if 0<=y-i<8 and 0<=x-i<8 and b[y-i][x-i]=='Q':
            return 0
        #右上チェック
        if 0<=y-i<8 and 0<=x+i<8 and b[y-i][x+i]=='Q':
            return 0
        #左下チェック
        if 0<=y+i<8 and 0<=x-i<8 and b[y+i][x-i]=='Q':
            return 0
    return 1

def sol(b,f,cnt):
    if cnt==8:
        return 1

#f行目に既にQがあったら他のQと干渉がないかをチェック
#干渉があればfalse扱いで終了、干渉がなければf+1で次の行へ
    if 'Q' in b[f]:
        if chk(b,f,b[f].index('Q'))==0:
            return 0
        else:
            sol(b,f+1,cnt)

#f行目にQがなければ0番目からQを仮に置いて干渉がなければ次の行へ
#干渉があれば仮置きのQを.に戻して同じf行目の右のマスでチェックする
    else:
        for p in range(8):
            b[f][p]='Q'
            cnt+=1
            if chk(b,f,p):
                sol(b,f+1,cnt)
            else:
                b[f][p]='.'
                cnt-=1


b=[]
cnt=0
for a in range(8):
    tmp=raw_input()
    cnt+=tmp.count('Q')
    if tmp.count('Q')>1:
        print 'No Answer'
        exit()
    b.append(list(tmp))

#初期配置で干渉があったらNoで終了
for a,i in enumerate(b):
    if 'Q' in i and chk(b,y,i.index('Q'))==0:
        print 'No Answer'
        exit()

sol(b,0,cnt)
for a,i in enumerate(b):
    if 'Q' not in i or chk(b,a,i.index('Q'))==0:
        print 'No Answer'
        exit()
for i in b:
    print ''.join(i)
