#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)
#define sl3(a,b,c)  scanf("%lld %lld %lld",&a,&b,&c)


vector <int> bitm(int bit,int n) {
    vector <int> s;
    rep(i,n) {
        if (bit & (1<<i)) s.push_back(0);
        else s.push_back(1);
    }
    return s;
}

int main(){
    int n,m,ans=0;
    sc1(n);
    int w[17][17];
    rep(i,17) rep(j,17) w[i][j]=3;
    rep(i,n) {
        int a;
        sc1(a);
        rep(j,a) {
            int x,y;
            sc2(x,y);
            w[i][x-1]=y;
        }
    }

    for (int i=0;i<32678;i++) {
        vector <int> d=bitm(i,15);
        int cnt=0,f=1;
        rep(j,n) cnt+=(d.at(j)==1);
        rep(j,n) rep(k,n) {
            if (d.at(j)==1 && w[j][k]==1 && d.at(k)==0) f=0;
            if (d.at(j)==1 && w[j][k]==0 && d.at(k)==1) f=0;
        }
        if (f) ans=max(ans,cnt);
    }
    printf("%d\n",ans);
    return 0;
}
