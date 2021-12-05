#include<bits/stdc++.h>
using namespace std;

#define sl1(a)  scanf("%lld",&a)

int main(){
    long long  n,ans;
    sl1(n);
    ans=n;
    for(long long i=2ll;i*i<=n;i++) {
        if (n%i==0ll)  {
            ans=i;
        }
        //cout << ans << " " << i<<endl;
        //if (i!=2)i++;
    }
    //cout<<ans<<endl;
    printf("%lld\n",ans+(n/ans)-2);
    return 0;
}
