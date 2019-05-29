#include<bits/stdc++.h>
using namespace std;
//from
//https://atcoder.jp/contests/abc110/submissions/3254887

const int mod=1e9+7;

struct com {
    int mod;
    vector<long long> mfact, rfact;

    com(int sz, int mod) : mfact(sz+1), rfact(sz+1), mod(mod) {
        mfact[0]=1;
        for (int i=1;i<mfact.size();i++) mfact[i]=mfact[i-1]*i%mod;
        rfact[sz]=inv(mfact[sz]);
        for (int i=sz-1;i>=0;i--) rfact[i]=rfact[i+1]*(i+1)%mod;
    }
    long long fact(int k) const {
        return (mfact[k]);
    }

    long long pow(long long x,long long n) const {
        long long ret=1ll;
        while(n>0) {
            if (n&1) (ret*=x)%=mod;
            (x*=x)%=mod;
            n>>=1;
        }
        return (ret);
    }
    long long inv(long long x) const {
        return (pow(x,mod-2));
    }

    long long P(int n, int r) const {
        if (r<0||n<r) return (0);
        return (mfact[n]*rfact[n-r]%mod);
    }

    long long C(int p,int q) const {
        if (q<0||p<q) return (0);
        return (mfact[p]*rfact[q]%mod*rfact[p-q]%mod);
    }

    long long H(int n, int r) {
        if(n<0||r<0) return (0);
        return (r==0?1:C(n+r-1,r));
    }
};

map<int, int> dp[32];

int rec(int x, int rest) {
    if(x==1) return rest==0;
    if(rest<=0) return 0;
    if(dp[rest].count(x)) return dp[rest][x];
    int ret=0;

    vector<int> div;
    for(int i=1;i*i<=x;i++) {
        if (x%i==0) {
            div.emplace_back(i);
            if(i*i!=x) div.emplace_back(x/i);
        }
    }
    
    for (auto &p:div) {
        if (x!=p) (ret+=rec(p, rest-1))%=mod;
    }
    return dp[rest][x]=ret;
}

int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    com beet(n+1,mod);
    int ret=0;
    for (int i=0;i<=min(31,n);i++) {
        int rest=n-1;
        auto add = beet.C(n,i);
        (add*=rec(m,i))%=mod;
        (ret+=add)%=mod;
    }
    printf("%d\n",ret);
}
