#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,k,h,ans=0;
    sc2(n,k);
    rep(i,n) {
        sc1(h);
        ans+=(h>=k);
    }
    printf("%d\n",ans);
    return 0;
}
