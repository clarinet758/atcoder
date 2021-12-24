#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)


int main(){
    int k;
    sc1(k);
    long long ans=0ll;
    for (int i=1;i<=k;i++) for (int j=1;j<=k;j++) for (int p=1;p<=k;p++) ans+=__gcd(__gcd(i,j),p);
    printf("%lld\n",ans);
    return 0;
}
