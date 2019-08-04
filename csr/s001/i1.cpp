#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    scanf("%d",&n);
    vector<int> a(n);
    for (auto &e:a) scanf("%d",&e);
    int ans=0,l=0,r=0,chk=a[0];
    for(;;) {
        if (chk==n) ans++;
        if (chk<n && r<n-1) {
            r++;
            chk+=a[r];
        } else if (chk>=n) {
            chk-=a[l];
            l++;
        } else {
            break;
        }
    }
    printf("%d\n",ans);
    return 0;
}
