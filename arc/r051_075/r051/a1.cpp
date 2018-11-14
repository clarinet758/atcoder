#include<bits/stdc++.h>
using namespace std;
//WAAAAAAAAAAAAAAA
int main(){
    int x,y,r;
    int x2,y2,x3,y3;
    scanf("%d %d %d",&x,&y,&r);
    scanf("%d %d %d %d",&x2,&y2,&x3,&y3);
    printf("%s\n",(x2<=x-r && x+r<=x3 && y2<=y-r && y+r<=y3)?"NO":"YES");
    printf("%s\n",(r*r>=(x2-x)*(x2-x)+(y2-y)+(y2-y) && r*r>=(x2-x)*(x2-x)+(y3-y)*(y3-y) && r*r>=(x3-x)*(x3-x)+(y2-y)*(y2-y) && r*r>=(x3-x)*(x3-x)*(y3-y)*(y3-y)?"NO":"YES"));
    return 0;
}
