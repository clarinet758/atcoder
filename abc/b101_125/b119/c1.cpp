#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int himo[10];
int mod=1000000007;
int n,a,b,c,l[10],ans=mod;

void cal(int x){
    if (x==-1) {
        int cnt=0,chk[3]={0,0,0};
        rep(i,n){
            if (himo[i]<3) {
                int w=himo[i];
                if (chk[w]>0) cnt+=10;
                chk[w]+=l[i];
            }
        }
        if (chk[0]>0 && chk[1]>0 && chk[2]>0) ans=min(ans,cnt+abs(a-chk[0])+abs(b-chk[1])+abs(c-chk[2]));
        return;
    }
    rep(i,4) {
        himo[x]=i;
        cal(x-1);
    }
}

int main(){
    scanf("%d %d %d %d",&n,&a,&b,&c);
    rep(i,n) scanf("%d",&l[i]);
    cal(n);
    printf("%d\n",ans);
    return 0;
}
