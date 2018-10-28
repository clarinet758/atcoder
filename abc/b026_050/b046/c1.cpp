#include<bits/stdc++.h>

using namespace std;

int main(){
    long long x,y;
    int n,t,a;
    scanf("%d",&n);
    scanf("%lld %lld",&x,&y);
    for (int i=1;i<n;i++) {
        scanf("%d %d",&t,&a);
        if (x<=t && y<=a) {
            x=t;
            y=a;
        } else {
            x=t*max((x+t-1)/t,(y+a-1)/a);
            y=a*max((x+t-1)/t,(y+a-1)/a);
        }
    }
    printf("%lld\n",x+y);
    return 0;
}
