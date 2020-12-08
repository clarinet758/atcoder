#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

long long x,dp[20][2];

long long cnt(char s[25],bool p) {
    bool f=0;
    x=0ll;
    rep(i,20) {dp[i][0]=0; dp[i][1]=0;}
    dp[0][0]=1ll;
    long l=strlen(s);
    for (long i=0;i<l;i++) {
        x*=10;
        int pt=s[i]-'0';
        x+=pt;
        if (pt==4 || pt==9) f=1;
        rep(j,10) {
            if (j==4 || j==9) continue;
            if (pt==j) dp[i+1][0]+=dp[i][0];
            if (pt>j) dp[i+1][1]+=dp[i][0];
            if (i>0l) { dp[i+1][1]+=dp[i][1]; }

        }
    }
    return x-dp[l][0]-dp[l][1]+1-(p==1 && f==1);
}

int main(){
    int n,m;
    char a[25],b[25];
    scanf("%s %s",a,b);
    long long ans=cnt(b,0)-cnt(a,1);
    printf("%lld\n",ans);
    return 0;
}
