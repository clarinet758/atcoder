#include<bits/stdc++.h>
using namespace std;

const int MAXn=100;
const int INFTY=1<<21;

int n,M[MAXn][MAXn],col[MAXn],d[MAXn],p[MAXn];

void dijkstra (int s) {
    for (int i=0;i<n;i++) {
        col[i]=0;
        d[i]=INFTY;
    }
    d[s]=0;
    p[s]=-1;
    for (;;) {
        int mincost=INFTY;
        int u;
        for (int i=0;i<n;i++) {
            if (col[i]!=2 && d[i]<mincost) {
                mincost=d[i];
                u=i;
            }
        }
        if (mincost==INFTY) break;
        col[u]=2;
        for (int v=0;v<n;v++) {
            if (col[v]!=2 && M[u][v]<d[v]) {
                if (d[u]+M[u][v]<d[v]) {
                    d[v]=d[u]+M[u][v];
                    p[v]=u;
                    col[v]=1;
                }
            }
        }
    }
    for (int i=0;i<n;i++) cout<<i<<" "<<(d[i]==INFTY?-1:d[i])<<endl;
    return;
}
/**
5 //頂点数
0 3 2 3 3 1 1 2 //それぞれの頂点と隣接する頂点と移動コスト
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3

**/
int main(){
    int mod=1000000007;
    //int n,h,w,t,ans;
    scanf("%d",&n);
    //char 
    //scanf("%d %d %d",&h,&w,&t);
    //printf("%d\n",ans);
    int id,k,v,c;
    for (int i=0;i<n;i++) for (int j=0;j<n;j++) M[i][j]=INFTY;
    for (int i=0;i<n;i++) {
        cin>>id>>k;
        for (int j=0;j<k;j++) {
            cin>>v>>c;
            M[id][v]=c;
        }
    }
    dijkstra(0);
    return 0;
}
