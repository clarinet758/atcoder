#include<bits/stdc++.h>

using namespace std;

int main(){
    int n;
    long long x,t,ans=0;
    scanf("%d %lld",&n,&x);
    vector<long long> a(n);
    for (auto&e:a) scanf("%lld",&e);
    for (int i=1;i<n;i++) {
        if (a[i]+a[i-1]>x) {
            t=a[i]+a[i-1]-x;
            ans+=t;
            a[i]=a[i]-t<0?0:a[i]-t;
        }
    }
    printf("%lld\n",ans);
    return 0;
}
