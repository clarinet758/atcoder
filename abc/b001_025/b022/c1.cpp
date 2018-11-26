#include<bits/stdc++.h>
using namespace std;

typedef vector<vector<int> > Matrix;
const int INF=100000000;
Matrix d;

void warshall_floyd(int n) {
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            for (int k=0;k<n;k++)
                d[j][k]=min(d[j][k], d[j][i]+d[i][k]);
    }

int main(){
    int mod=1000000007;
    int n,m,x=0,ans=INF;
    scanf("%d %d",&n,&m);
    int b[n]={0};
    deque<int> q(n);
    d=Matrix(n, vector<int>(n,INF));
    for (int i=0;i<n;i++) d[i][i]=0;
    for (int i=0;i<m;i++) {
        int from,to,cost;
        scanf("%d %d %d",&from,&to,&cost);
        if (from!=1) {
            d[from-1][to-1]=cost;
            d[to-1][from-1]=cost;
        } else {
            b[to-1]=cost;
            q.push_front(to-1);
            x++;

        }
    }
    warshall_floyd(n);
    for (int i=0;i<x-1;i++) {
        for (int j=i+1;j<x;j++) {
            int from=min(q[i],q[j]);
            int to=max(q[i],q[j]);
            if (d[from][to]!=0) {
                ans=min(ans,d[from][to]+b[from]+b[to]);
            }
        }
    }
    printf("%d\n",ans!=INF?ans:-1);
    return 0;
}
