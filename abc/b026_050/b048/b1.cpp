#include<bits/stdc++.h>

using namespace std;

int main(){
    long long a,b,x;
    scanf("%lld %lld %lld",&a,&b,&x);
    printf("%lld\n",(b/x)-(a/x)+(a%x==0?1:0));
    return 0;
}
