#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int x1,y1,x2,y2,x3,y3,a,b,c,d;
    double ans;
    scanf("%d %d %d %d %d %d",&x1,&y1,&x2,&y2,&x3,&y3);
    a=x2-x1;
    b=y2-y1;
    c=x3-x1;
    d=y3-y1;
    ans = abs(a*d-b*c)/2.0;
    printf("%.11f\n",ans);
    return 0;
}
