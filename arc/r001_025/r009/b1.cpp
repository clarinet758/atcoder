#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,w[15];
    rep(i,10)  sc1(w[i]);
    sc1(n);
    vector<int> a(n);
    map<int, int> ans;
    rep(i,n) {
        int p;
        sc1(p);
        int x=p,y=0,z=1;
        while(x>0) {
            int now;
            rep(j,10) if (x%10==w[j]) now=j;
            y+=now*z;
            x/=10;
            z*=10;
        }
        ans.insert(make_pair(y,p));
        a[i]=y;
    }
    sort(a.begin(),a.end());
    rep(i,n) printf("%d\n",ans[a[i]]);
    return 0;
}
