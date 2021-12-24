#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

bool w[100005];
int  t[100005];
int main(){
    int n,m,ac=0,wa=0;
    sc2(n,m);
    rep(i,m) {
        int x;
        string y;
        cin >> x >> y;
        if (y=="AC" && w[x]==0) {
            w[x]=1;
        } else if (y=="WA" && w[x]==0) {
            t[x]++;
        }
    }
    rep(i,n) {
        if (w[i+1]){
            ac++;
            wa+=t[i+1];
        }
    }
    printf("%d %d\n",ac,wa);
    return 0;
}
