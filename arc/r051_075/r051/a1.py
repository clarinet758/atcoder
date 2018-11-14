
x,y,r=map(int, input().split())
x2,y2,x3,y3=map(int, input().split())

print("NO" if (x2<=x-r and x+r<=x3 and y2<=y-r and y+r<=y3) else "YES")
r*=r
print("NO" if (r>=((x2-x)**2)+((y2-y)**2) and r>=((x2-x)**2)+((y3-y)**2) and r>=((x3-x)**2)+((y2-y)**2) and r>=((x3-x)**2)+((y3-y)**2)) else "YES")
#r*r>=(x2-x)*(x2-x)+(y2-y)+(y2-y) && r*r>=(x2-x)*(x2-x)+(y3-y)*(y3-y) && r*r>=(x3-x)*(x3-x)+(y2-y)*(y2-y) && r*r>=(x3-x)*(x3-x)*(y3-y)*(y3-y)?"NO":"YES"));
