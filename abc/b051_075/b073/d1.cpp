#include<bits/stdc++.h>
using namespace std;

#define PI 3.1415926535897932
#define inf 1<<29

int n,m,r;
int d[201][201];
int w[9];
int a,b,c;
int res;
bool used[9];

void dfs(int c,int las,int dist) {
    if (c==r+1) {
        if (res>dist) res=dist;
        return;
    }

    for (int i=1;i<=r;i++) if (!used[i]) {
        used[i]=true;
        if (las==-1) dfs(c+1,i,0);
        else dfs(c+1,i,dist+d[w[las]][w[i]]);
        used[i]=false;
    }
}

int main(){
    scanf("%d %d %d",&n,&m,&r);
    for (int i=1;i<=n;i++) for (int j=1;j<=n;j++) if (i!=j) d[i][j]=inf;
    for (int i=1;i<=r;i++) scanf("%d",&w[i]);
    for (int i=1;i<=m;i++) {
        scanf("%d %d %d",&a,&b,&c);
        if (d[a][b]>c) d[a][b]=d[b][a]=c;
    }
    for (int k=1;k<=n;k++) for (int i=1;i<=n;i++) for (int j=1;j<=n;j++) {
        if (d[i][j]>d[i][k]+d[k][j]) d[i][j]=d[i][k]+d[k][j];
    }
    res=inf;
    dfs(1,-1,0);
    printf("%d\n",res);
    return 0;
}
