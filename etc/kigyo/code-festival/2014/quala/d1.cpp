#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

long long dp[18][3];
bool lg[10],nn[10],sm[10];

int chk(long long x) {
    //cout <<x<<endl;
    int cv=0; bool cc[10];
    rep(i,10) cc[i]=0;
    while (x>0) {
        if(cc[x%10]==0) {cc[x%10]=1; cv++;}
        x/=10;
    }
    return cv;
}

int main(){
    long long mmm=2e15+5;;
    char s[20];
    int k;
    scanf("%s %d",s,&k);
    long n=strlen(s);
    rep(i,18) dp[i][2]=mmm;
    dp[0][2]=0;
    for (long i=0l;i<n;i++) {
        long long  t=s[i]-'0';
        dp[i+1][1]=dp[i][1]*10+t;
        rep(j,10) {
            long long smp=dp[i][0]*10+(j*1ll), tmp=dp[i][1]*10+(j*1ll), lmp=dp[i][2]*10+(j*1ll);
            if (tmp<dp[i+1][1] && chk(tmp)<=k)  dp[i+1][0] = max(dp[i+1][0],tmp);
            if (smp<dp[i+1][1] && chk(smp)<=k)  dp[i+1][0] = max(dp[i+1][0],smp);
            if (tmp>dp[i+1][1] && chk(tmp)<=k)  dp[i+1][2] = min(dp[i+1][2],tmp);
            if (lmp>dp[i+1][1] && chk(lmp)<=k)  dp[i+1][2] = min(dp[i+1][2],lmp);
        }
    }
    if (chk(dp[n][1])<=k) printf("0\n");
    else printf("%lld\n",((dp[n][1]-dp[n][0])<(dp[n][2]-dp[n][1]))?dp[n][1]-dp[n][0]:dp[n][2]-dp[n][1]);
    return 0;
}
