#include<bits/stdc++.h>
using namespace std;

//WA!!!!!!!!!!!!!!
int main(){
    int n;
    long long chk1,chk2,ans1=0,ans2=0;
    scanf("%d",&n);
    vector<long> a(n);
    for (auto&e:a) scanf("%ld",&e);
    chk1=a[0]+a[1];
    chk2=a[0]+a[1];
    if (chk1<=0) {
        ans1=-1*chk1+1;
        chk1=1;
    }
    if (chk2>=0) {
        ans2=chk2+1;
        chk2=-1;
    }

    for (int i=2;i<n;i++) {
        chk1+=a[i];
        chk2+=a[i];
        if (i%2) {
            if (chk1<=0) {
                ans1+=-1*chk1+1;
                chk1=1;
            }
            if (chk2>=0) {
               ans2+=chk2+1;
               chk2=-1;
            }
        } else {
            if (chk1>=0) {
                ans1+=chk1+1;
                chk1=-1;
            }
            if (chk2<=0) {
                ans2+=-1*chk2+1;
                chk2=1;
            }
        }
    }
    if (
    printf("%lld\n",min(ans1,ans2));
    return 0;
}
