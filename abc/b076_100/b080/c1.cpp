#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    scanf("%d",&n);
    bool f[n][10];
    int p[n][11];
    int cnt[n]={0};
    long long ans=0;
    for (int i=0;i<n;i++) for (int j=0;j<10;j++) {
        cin>>f[i][j];
    }
    for (int i=0;i<n;i++) for (int j=0;j<11;j++) cin>>p[i][j];

    long long tmp;
    for (int i=1;i<(1<<10);i++) {
        tmp=0;
        for (int x=0;x<n;x++) cnt[x]={0};
        for (int j=0;j<10;j++) {
            if (i&(1<<j)) for (int k=0;k<n;k++) if (f[k][j]) cnt[k]++;
        }
        for (int l=0;l<n;l++) tmp+=p[l][cnt[l]];
        if (i==1) ans=tmp;
        else ans=max(ans,tmp);
    }
    printf("%lld\n",ans);
    return 0;
}
