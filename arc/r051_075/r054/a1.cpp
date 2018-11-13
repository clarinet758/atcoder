#include<bits/stdc++.h>
using namespace std;

#define PI 3.1415926535897932

int main(){
    double l,x,y,s,d,ans;
    scanf("%lf %lf %lf %lf %lf",&l,&x,&y,&s,&d);
    if (s>d) {
        ans=(l-(s-d))/(x+y);
        if (x<y) ans=min(ans,(s-d)/(y-x));
    } else {
        ans=(d-s)/(x+y);
        if (x<y) ans=min(ans,(l-(d-s))/(y-x));
    }
    printf("%.10lf\n",ans);
    return 0;
}
