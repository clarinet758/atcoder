#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sl3(a,b,c)  scanf("%lld %lld %lld",&a,&b,&c)

int main(){
    long long  n,a,b,ans;
    sl3(n,a,b);
    ans=n/(a+b) * a;
    ans+=min(a,n%(a+b));
    cout << ans << endl;
    return 0;
}
