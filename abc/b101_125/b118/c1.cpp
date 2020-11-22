#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

set <int> a; set <int> b;

int main(){
    int mod=1000000007;
    int x,n,p=mod,cnt=0,tmp1=mod,tmp2=mod;
    sc1(n);
    rep(i,n) {
        sc1(x);
        tmp1=min(tmp1,x);
        a.insert(x);
    }
    for(;;) {
        cnt++;
        if (cnt%2) {
            for (;;) {
                if (a.size()==0) break;
                auto bb = *a.begin();
                b.insert(bb%tmp1?bb%tmp1:tmp1);
                tmp2=min(tmp2,bb%tmp1?bb%tmp1:tmp1);
                a.erase(a.begin());
            }
            tmp1=mod;
        } else {
            for(;;) {
                if (b.size()==0) break;
                auto aa = *b.begin();
                a.insert(aa%tmp2?aa%tmp2:tmp2);
                tmp1=min(tmp1,aa%tmp2?aa%tmp2:tmp2);
                b.erase(b.begin());
            }
            tmp2=mod;
        }
        if (a.size()==1) { printf("%d\n",tmp1); break; }
        else  if (b.size()==1) { printf("%d\n",tmp2); break; }
    }
    return 0;
}
