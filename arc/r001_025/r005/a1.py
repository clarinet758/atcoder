#!/usr/bin/python


N=int(raw_input())
i=map(str,raw_input()[:-1].split())
l=0
for x in i:
    if x=="TAKAHASHIKUN" or x=="Takahashikun" or x=="takahashikun":
        l+=1
print l
#print len(re.findall("^TAKAHASHIKUN\s|^Takahashikun\s|^takahashikun\s\
#                |\sTAKAHASHIKUN\.$|\sTakahashikun\.$|\stakahashikun\.$\
#                |\sTAKAHASHIKUN\s|\sTakahashikun\s|\stakahashikun\s\
#                |^TAKAHASHIKUN\.$|^Takahashikun\.$|^takahashikun\.$",i))
