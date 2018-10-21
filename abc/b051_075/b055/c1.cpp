#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    long long n,m,ans=0;
    scanf("%lld %lld",&n,&m);
    ans=(n*2<=m?n:m/2)+(n*2<=m?(m-n*2)/4:0);
    printf("%lld\n",ans);
    return 0;
}
