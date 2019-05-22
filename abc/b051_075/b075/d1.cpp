#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    int n,k;
    scanf("%d %d",&n,&k);
    vector<int> x(n),y(n);
    vector<int> xary,yary;

    for (int i=0;i<n;++i) {
        scanf("%d %d",&x[i],&y[i]);
        xary.push_back(x[i]);
        yary.push_back(y[i]);
    }
    sort(begin(xary), end(xary));
    sort(begin(yary), end(yary));
    long long ans=1ll*(xary[n-1]-xary[0])*(yary[n-1]-yary[0]);
    for (int xi=0;xi<n;++xi) {
        for (int xj=xi+1;xj<n;++xj) {
            for (int yi=0;yi<n;++yi) {
                for (int yj=yi+1;yj<n;++yj) {
                    int num=0;
                        long long lx=xary[xi],rx=xary[xj];
                        long long by=yary[yi],uy=yary[yj];
                        for (int i=0;i<n;++i) if(lx<=x[i] and x[i]<=rx and by<=y[i] and y[i]<=uy) num++;
                        if (num>=k) ans=min(ans,1ll*(rx-lx)*(uy-by));
                }
            }
        }
    }
    printf("%lld\n",ans);
    return 0;
}
