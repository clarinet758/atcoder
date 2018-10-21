#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    int mod=1000000007;
    int n;
    long long ans=1;
    scanf("%d",&n);
    for (int i=1;i<=n;i++) {
        ans*=i;
        ans%=mod;
    }
    printf("%lld\n",ans);
    return 0;
}
