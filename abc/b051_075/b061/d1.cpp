#include<bits/stdc++.h>
using namespace std;

const long long inf=1ll<<50;
int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    const int nmax=1000;
    const int mmax=2000;
    int a[mmax],b[mmax];
    long long c[mmax];

    for (int i=0;i<m;++i) {
        scanf("%d %d %lld",&a[i],&b[i],&c[i]);
        c[i]=-c[i];
    }

    long long dist[nmax];

    for (int i=0;i<n;++i) dist[i]=inf;
    dist[0]=0;
    
    for (int loop=0;loop<n-1;++loop) {
        for (int i=0;i<m;++i) {
            if (dist[a[i]-1]==inf) continue;

            if (dist[b[i]-1]>dist[a[i]-1]+c[i]) {
                dist[b[i]-1]=dist[a[i]-1]+c[i];
            }
        }
    }
    long long ans=dist[n-1];

    bool nega[nmax];
    for (int i=0;i<n;++i) nega[i]=false;

    for (int loop=0;loop<n;++loop) {
        for (int i=0;i<m;++i) {
            if (dist[a[i]-1]==inf) continue;

            if (dist[b[i]-1]>dist[a[i]-1]+c[i]) {
                dist[b[i]-1]=dist[a[i]-1]+c[i];
                nega[b[i]-1]=true;
            }
            if (nega[a[i]-1]==true) {
                nega[b[i]-1]=true;
            }
        }
    }

    if (nega[n-1]) printf("inf\n");
    else printf("%lld\n",-ans);
    
    return 0;
}
