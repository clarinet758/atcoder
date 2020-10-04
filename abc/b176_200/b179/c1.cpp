#include<bits/stdc++.h>
using namespace std;

#define sl1(a)  scanf("%lld",&a)

int main(){
    long long n,ans=0ll;
    sl1(n);
    for (long long  i=1;i<=n;i++) {
        for (long long j=i;j<=n;j++) {
            if (n-(i*j)>0) {
                ans++;
                if (i!=j) ans++;
            }else{
                break;
            }
        }
    }
    printf("%lld\n",ans);
    return 0;
}
