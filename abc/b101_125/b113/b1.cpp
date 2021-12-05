#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int mod=1000000007;
    int n,t,a,m,ans,chk=mod*2;
    sc1(n);
    sc2(t,a);
    t*=1000; a*=1000;
    rep(i,n) {
        sc1(m);
        //cout << abs(a-(t-m*6)) << endl;
        if (chk>abs(a-(t-m*6))) {
            chk=abs(a-(t-m*6));
            ans=i+1;
        }

    }
    printf("%d\n",ans);
    return 0;
}
