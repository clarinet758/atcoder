#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int h[105];
int main(){
    int n,x=101,ans=0;
    sc1(n);
    rep(i,n){
        sc1(h[i]);
        x=min(x,h[i]);
    }
    ans=x;
    rep(i,n) h[i]-=x;

    for(;;) {
        int l=-1,r=-1,xx=101;
        rep(i,n+1){
            if (h[i]>0 && l==-1) l=i;
            if (h[i]==0 && l>-1) {r=i; break;}
            if (l>-1) xx=min(xx,h[i]);
        }
        if (l==-1) break;
        ans+=xx;
        for(int i=l;i<r;i++) {
            h[i]-=xx;
        }
    }
    printf("%d\n",ans);
    return 0;
}
