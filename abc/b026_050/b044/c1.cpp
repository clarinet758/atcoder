#include<bits/stdc++.h>

using namespace std;
//部分点のみ用
int main(){
    int n,a,cnt,ttl;
    long long ans=0;
    scanf("%d %d",&n,&a);
    vector<int> x(n);
    for (auto&e:x) scanf("%d",&e);

    for (int i=0;i<(1<<n);i++) {
        cnt=0;
        ttl=0;
        for (int j=0;j<n;j++) {
            if (i & (1<<j)) {
                cnt++;
                ttl+=x[j];
            }
        }
        if (cnt*a==ttl && ttl!=0) ans++;
    }
    printf("%lld\n",ans);

    return 0;
}
