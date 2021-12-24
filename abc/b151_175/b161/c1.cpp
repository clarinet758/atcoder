#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)
#define sl3(a,b,c)  scanf("%lld %lld %lld",&a,&b,&c)
#define PI 3.1415926535897932

int main(){
    long long n,k,ans=1e18+3;
    sl2(n,k);
    if (n>=k) {
        ans=min(ans,n%k);
        n=n%k;
    }
    ans=min(ans,abs(n-k));
    n=abs(n-k);
    ans=min(ans,abs(n-k));
    printf("%lld\n",ans);
    return 0;
}
