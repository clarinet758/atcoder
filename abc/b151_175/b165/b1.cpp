#include<bits/stdc++.h>
using namespace std;

#define sl1(a)  scanf("%lld",&a)

int main(){
    long long x,t=100,ans=0ll;
    sl1(x);
    for(;;) {
        ans++;
        t+=t/100;
        if (t>=x) break;
    }
    printf("%lld\n",ans);
    return 0;
}
