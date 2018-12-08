s=input()
ans=[]
for i in s:
    if len(ans) and i=='B': ans.pop()
    elif i!='B': ans.append(i)
print(''.join(ans))
