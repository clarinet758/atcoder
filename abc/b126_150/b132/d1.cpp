#include<bits/stdc++.h>
using namespace std;
 
const long long  MAX=510000;
const long long MOD=1000000007;
 
long long fac[MAX], finv[MAX], inv[MAX];

void COMinit() {
    fac[0]=fac[1]=1;
    finv[0]=finv[1]=1;
    inv[1]=1;
    for (long long i=2;i<MAX;i++) {
        fac[i]=fac[i-1]*i%MOD;
        inv[i]=MOD-inv[MOD%i]*(MOD/i)%MOD;
        finv[i]=finv[i-1]*inv[i]%MOD;
    }
}
long long COM(int n,int k) {
    if (n<k) return 0;
    if (n<0 || k<0) return 0;
    return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD;
}
int main(){
    COMinit();
    long long n,k,ans=0ll;
    scanf("%lld %lld",&n,&k);
    for (long long i=1;i<=k;i++) {
        if (i>1) {
            ans=(COM(n+1-k,i)*COM(k-1,i-1))%MOD;
        } else {
            ans=COM(n+1-k,i);
        }
        printf("%lld\n",ans%MOD);
    }
    return 0;
}
