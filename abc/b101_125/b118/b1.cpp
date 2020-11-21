#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)


int ans[35];

int main(){
    int mod=1000000007;
    int n,m,cnt=0;
    int k,p;
    sc2(n,m);
    rep(i,n) {
        sc1(k);
        rep(j,k) {
            sc1(p);
            ans[p]+=1;
        }
    }
    rep(i,33) if(ans[i]==n) cnt++;
    printf("%d\n",cnt);
    return 0;
}
