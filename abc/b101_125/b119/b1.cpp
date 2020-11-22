#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int mod=1000000007;
    int n,m;
    double ans=0.0;
    sc1(n);
    rep(i,n) {
        double p;
        char s[5];
        scanf("%lf %s",&p,s);
        if (s[0]=='J') ans+=p;
        else ans+=p*380000.0;
    }
    printf("%.15lf\n",ans);
    return 0;
}
