#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,m;
    sc2(n,m);
    int cd[n+5];
    rep(i,n+4) cd[i]=i;
    rep (i,m) {
        int p;
        sc1(p);
        cd[n+1]=cd[0];
        cd[0]=p;
        rep(j,n) if (cd[j+1]==p) cd[j+1]=cd[n+1];
    }
    rep(i,n) printf("%d\n",cd[i+1]);
    return 0;
}
