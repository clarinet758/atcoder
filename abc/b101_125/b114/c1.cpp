#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sl1(a)  scanf("%lld",&a)

long long n,ans;
bool p[13];
map <int ,long long> v;
bool chk(int a) {
    bool d[3]={0,0,0};
    while(a>0) {
        if(a%10==3) d[0]=1;
        if(a%10==5) d[1]=1;
        if(a%10==7) d[2]=1;
        a/=10;
    }
    if (d[0]==1 && d[1]==1 && d[2]==1) return 1;
    else return 0;
}
void sol(long long x){
    rep(i,3) {
        x*=10;
        x+=v[i];
        if (x>n) return;
        if (chk(x)) ans++;
        sol(x);
        x/=10;
    }
}
int main(){
    sl1(n);
    v[0]=3ll;v[1]=5ll;v[2]=7ll;
    sol(0ll);
    printf("%lld\n",ans);
    return 0;
}
