#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    int n,k,ans,tmp=0;
    scanf("%d %d",&n,&k);
    vector<int> a(n);
    for (int i=0;i<n;i++) {
        scanf("%d",&a[i]);
        if (a[i]==k) {
            printf("POSSIBLE\n");
            return 0;
        }
        if (i>0) tmp=max(tmp,a[i-1]);
    }
        
    if (tmp<k) {
        printf("IMPOSSIBLE\n");
        return 0;
    }
    sort(a.begin(),a.end());
    tmp-=k;
    for (int i=1;i<n;i++) {
        int t=a[i]-a[i-1];
        if (t) tmp%=t;
    }

    printf("%s\n",tmp==0?"POSSIBLE":"IMPOSSIBLE");
    return 0;
}
