#include<bits/stdc++.h>
using namespace std;

int main(){
    long long ans,o=1,p=1,mod=1000000007;
    int n,m;
    scanf("%d %d",&n,&m);
    if (abs(n-m)>1) {
        printf("0\n");
    } else {
        for (int i=1;i<=min(n,m);i++) {
            o*=i;
            p*=i;
            o%=mod;
            p%=mod;
        }
        if (abs(n-m)%2) {
            o*=max(n,m);
            o%=mod;
            ans=(o*p)%mod;
        } else {
            ans=(o*p*2)%mod;
        }
        printf("%lld\n",ans);
    }
    return 0;
}
