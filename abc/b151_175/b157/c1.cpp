#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

bool w[20];
int main(){
    int n,m;
    sc2(n,m);
    vector <int> ans(n,0);
    if (n!=1) ans.at(0)=1;
    rep(i,m) {
        int s,c;
        sc2(s,c);
        if (((s==1 && c==0)&&(n!=1))  || (w[s]==1 && ans.at(s-1)!=c)) { printf("-1\n"); return 0; }
        w[s]=1;
        ans.at(s-1)=c;
    }
    rep(i,n) printf("%d",ans.at(i));
    puts("");
    return 0;
}
