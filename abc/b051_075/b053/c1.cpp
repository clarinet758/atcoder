#include<bits/stdc++.h>
using namespace std;

int main(){
    long long x,ans;
    scanf("%lld",&x);
    x--;
    ans=x/11*2;
    printf("%lld\n",x%11<6?ans+1:ans+2);
    return 0;
}
