#include<bits/stdc++.h>
using namespace std;

// from https://atcoder.jp/contests/abc138/submissions/7012551
vector<int> to[200005];
vector<int> ans;

void dfs(int v,int p=-1) {
    for (int u:to[v]) {
        if (u==p) continue;
        ans[u]+=ans[v];
        dfs(u,v);
    }
}


int main(){
    int mod=1000000007;
    int n,q;
    scanf("%d %d",&n,&q);
    for (int i=1;i<n;i++) {
        int a,b;
        scanf("%d %d",&a,&b);
        --a; --b;
        to[a].push_back(b);
        to[b].push_back(a);
    }
    ans.resize(n);
    for (int i=0;i<q;i++) {
        int p,x;
        scanf("%d %d",&p,&x);
        --p;
        ans[p]+=x;
    }
    dfs(0);
    for (int i=0;i<n;i++) printf("%d\n",ans[i]);
    return 0;
}
