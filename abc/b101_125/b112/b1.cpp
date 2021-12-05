#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,m,t,ans=11111;
    sc2(n,t);
    rep(i,n) {
        int a,b;
        sc2(a,b); 
        if  (t>=b) ans=min(ans,a);
    }
    if (ans==11111) printf("TLE\n");
    else printf("%d\n",ans);
    return 0;
}
