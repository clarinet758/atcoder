#!/usr/bin/env python
# -*- coding: UTF-8 -*-

m=int(raw_input())
ans=chk=0
if m<100:
    print '00'
elif m<=5000:
    print '0'+str(m/100) if m<1000 else str(m/100)
elif m<=30000:
    print m/1000+50
elif m<=70000:
    print ((m/1000)-30)/5+80
else:
    print 89	
