n=int(raw_input())
 
def age(p):
    p+=100
    p-=p%100
    return p
 
def tasu(q):
    return q-(q%5)+5
 
def hiku(r):
    return r-(r%5)
 
def form(s):
    s=str(s)
    return '0'*(4-len(s))+s
l=[]
for i in range(n):
    a,b=map(int,raw_input().split('-'))
    a=hiku(a)
    if b%100>55:
        b=age(b)
    elif b%100<55 and b%5!=0:
        b=tasu(b)
    l.append([a,b])
l.sort()
ans=[]
for i in l:
    if len(ans)==0:
        ans.append(i)
    else:
        if ans[-1][1]<i[0]:
            ans.append(i)
        else:
            ans[-1][1]=max(ans[-1][1],i[1])
for i in ans:
    print form(i[0])+'-'+form(i[1])

