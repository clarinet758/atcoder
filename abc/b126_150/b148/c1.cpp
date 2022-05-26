#include<bits/stdc++.h>
using namespace std;

#define sc2(a,b)  scanf("%d %d",&a,&b)

long long lcm(int a,int b) { return 1ll*a*b/__gcd(a,b); }


int main(){
    int a,b;
    sc2(a,b);
    printf("%lld\n",lcm(a,b));
    return 0;
}
