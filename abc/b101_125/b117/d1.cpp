#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)
long long dp[60][2],w[60];
int cnt[60],kk[60]; 
int main(){
    long long n,k;
    sl2(n,k);
    w[0]=1;
    for(int i=1;i<60;i++)  w[i]=w[i-1]*2; 
    long long k1=k;
    rep(j,60) {
        if (k1&1) kk[j]+=1;
        k1=k1>>1;
    }
    for (long long i=0;i<n;i++) {
        long long a;
        sl1(a);
        rep(j,60) {
            if (a&1) cnt[j]+=1;
            a=a>>1;
        }
    }
    int f=0;
    for(int i=58;i>=0;i--) {
        if (f==1) f++;
        else if (f==0 && kk[i]==1) f=1;
        if (kk[i]==1) dp[i][0]=dp[i+1][0]+(w[i]*((n-cnt[i])*1ll));
        else if (kk[i]==0) dp[i][0]=dp[i+1][0]+(w[i]*(cnt[i]*1ll));
        long long y=max(cnt[i]*1ll,(n-cnt[i]*1ll))*w[i];
        if (f==1) dp[i][1]=(w[i]*(cnt[i]*1ll));
        else if (f>1) dp[i][1]=(dp[i+1][1]+y);
        if (f>1 && kk[i]==1) dp[i][1]=max(dp[i][1],dp[i+1][0]+(cnt[i]*1ll*w[i]));
    }
    printf("%lld\n",max(dp[0][0],dp[0][1]));
    return 0;
}
