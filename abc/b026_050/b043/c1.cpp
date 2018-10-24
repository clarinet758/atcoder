#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,chk,ans;
    scanf("%d",&n);
    vector<int> a(n);
    for(auto&e:a) scanf("%d",&e);
    for (int i=-100;i<101;i++) {
        chk=0;
        for (int j=0;j<n;j++) {
            chk+=abs(a[j]-i)*abs(a[j]-i);
        }
        if (i==-100) ans=chk;
        ans=min(ans,chk);
    }
    printf("%d\n",ans);

    return 0;
}
