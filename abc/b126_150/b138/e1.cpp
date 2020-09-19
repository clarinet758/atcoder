#include<bits/stdc++.h>
using namespace std;

// from https://atcoder.jp/contests/abc138/submissions/7013118
#define sz(x) int(x.size())


int main(){
    string s,t;
    cin >> s>>t;
    int n=sz(s),m=sz(t);
    vector<vector<int>> is(26);
    for (int i=0;i<n;i++) is[s[i]-'a'].push_back(i);
    for (int i=0;i<n;i++) is[s[i]-'a'].push_back(i+n);
    long long ans=0;
    int p=0;
    for (int i=0;i<m;i++) {
        int c=t[i]-'a';
        if (sz(is[c])==0) {
            puts("-1");
            return 0;
        }
        p=*lower_bound(is[c].begin(), is[c].end(),p)+1;
        if(p>=n){
            p-=n;
            ans+=n;
        }
    }
    ans+=p;
    printf("%lld\n",ans);
    return 0;
}
