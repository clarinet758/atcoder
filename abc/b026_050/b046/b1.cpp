#include<bits/stdc++.h>

using namespace std;

int main(){
    int mod=1000000007;
    int n,k;
    long long tmp=1;
    scanf("%d %d",&n,&k);
    for (int i=0;i<n-1;i++) {
        tmp*=k-1;
    }
    printf("%lld\n",tmp*k);
    return 0;
}
