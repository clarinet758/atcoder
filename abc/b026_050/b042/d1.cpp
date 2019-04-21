#include<bits/stdc++.h>
using namespace std;
 
const int MAX=510000;
const int MOD=1000000007;
 
long long fac[MAX], finv[MAX], inv[MAX];
 
void COMinit() {
    fac[0]=fac[1]=1;
    finv[0]=finv[1]=1;
    inv[1]=1;
    for (int i=2;i<MAX;i++) {
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
    long long  h,w,a,b,u,d,ans=0;
    scanf("%lld %lld %lld %lld",&h,&w,&a,&b);
 
    for (long long i=b+1;i<=w;i++) {
        u=COM(h-a+i-2,i-1)%MOD;
        d=COM(a+(w-i)-1,a-1)%MOD;
        ans+=(u*d)%MOD;
    }
    printf("%lld\n",ans%MOD);
    return 0;
}
