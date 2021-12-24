#include<bits/stdc++.h>
using namespace std;

#define sl3(a,b,c)  scanf("%lld %lld %lld",&a,&b,&c)

int main(){
    long long a,b,k;
    sl3(a,b,k);
    if (a>k) {
        a-=k;
    } else {
        k-=a;
        a=0;
        b-=k;
        if (b<0) b=0;
    }
    printf("%lld %lld\n",a,b);
    return 0;
}
