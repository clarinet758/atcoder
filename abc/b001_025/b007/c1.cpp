#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int n,m[100][100];
int color[100],d[100],f[100],tt;

void dfs_visit(int u) {
    int v;
    color[u]=1;
    d[u]=++tt;
    rep(v,n) {
        if(m[u][v]==0) continue;
        if(color[v]==0) dfs_visit(v);
    }
    color[u]=2;
    f[u]=++tt;
}

void dfs() {
    int u;
    rep(i,100) color[i]=0;
    tt=0;
    rep(i,n) if(color[i]==0) dfs_visit(i);
    rep(i,n) printf("%d %d %d\n",i+1,d[i],f[i]);
}

int main(){
    int u,c,v,ans;
    sc1(n);
    rep(i,n) rep(j,n) m[i][j]=0;
    rep(i,n) {
        sc2(u,c);
        u--;
        rep(j,c) {
            sc1(v);
            v--;
            m[u][v]=1;
        }
    }
    dfs();
    return 0;
}
