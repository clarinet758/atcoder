#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,ans=0,tmp=0;
    scanf("%d",&n);
    vector<long long> a(n);
    for (auto&e:a) scanf("%d",&e);
    for (int i=0;i<n;i++) {
        tmp=0;
        long long k=a[i];
        for(;;) {
            if (k>=1 && k%2==0) {
                k/=2;
                tmp++;
            } else {
                break;
            }
        }
        ans+=tmp;
    }
    printf("%d\n",ans);
    return 0;
}
