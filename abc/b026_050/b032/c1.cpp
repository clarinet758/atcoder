#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    int n,k;
    scanf("%d %d",&n,&k);
    vector<int> s(n);
    for (auto&e:s) scanf("%d",&e);
    int ans=0,chk=0,t=-1;
    long long p=1;
    for (int i=0;i<n;i++) {
        p*=s[i];
        chk++;
        if (s[i]==0) {
            ans=n;
            break;
        } else if (p<=k) {
            ans=max(ans,chk);
        } else {
            while(p>k && t<i) {
                t++;
                p/=s[t];
                chk--;
            }
            ans=max(ans,chk);
        }
    }
    printf("%d\n",ans);
    return 0;
}
