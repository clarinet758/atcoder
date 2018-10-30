#include<bits/stdc++.h>

using namespace std;

int main(){
    int mod=1000000007;
    int n;
    long long ans=0;
    scanf("%d",&n);

    vector<int> a(n);
    for (auto&e:a) scanf("%d",&e);
    sort(a.begin(),a.end());
    if (n%2) {
        for (int i=0;i<n;i++) {
            if (i==0 && a[i]==0) {
                ans=1;
            } else if (i==0 && a[i]!=0) {
                ans=0;
                break;
            } else if (i>0 && a[i]==i && a[i-1]==i) {
                ans*=2;
                ans%=mod;
            } else {
                ans=0;
                break;
            }
            i++;
        }
    } else {
        for (int i=1;i<n;i++) {
            if (i==1 && a[1]==1 && a[0]==1) {
                ans=2;
            } else if (i==1 && (a[i]!=1 || a[i-1]!=1)) {
                ans=0;
                break;
            } else if (i>1 && a[i]==i && a[i-1]==i) {
                ans*=2;
                ans%=mod;
            } else {
                ans=0;
                break;
            }
            i++;
        }
    }
    printf("%lld\n",ans);
    return 0;
}
