#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,m=map(int,raw_input().split())
tmp=n*3
if tmp==m:
    print 0,n,0
elif n*3<m<=4*n:
    print 0,n-m+tmp,m-tmp
elif  2*n<=m<3*n:
    print tmp-m,n-tmp+m,0
else:
    print -1,-1,-1
  
    
