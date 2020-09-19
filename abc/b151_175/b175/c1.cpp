#include<bits/stdc++.h>
using namespace std;

int main(){
    long long x,k,d;
    scanf("%lld %lld %lld",&x,&k,&d);
    x=abs(x);
    if (x/d>k) {
        printf("%lld\n",x%d+d*(x/d-k));
    } else {
        printf("%lld\n",(k-x/d)%2==0?x%d:abs(x%d-d));
    }
    return 0;
}
