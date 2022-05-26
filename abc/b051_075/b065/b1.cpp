#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

bool chk[100007];
int main(){
    int n,p=1,ans=0;
    sc1(n);
    vector <int>a(n+5);
    rep(i,n)  sc1(a[i]);
    rep(i,n+1) {
        ans++;
        if (a[p-1]==2) {
            printf("%d\n",ans);
            break;
        } else if (chk[p]) {
            printf("-1\n");
            break;
        } else {
            chk[p]=1;
            p=a[p-1];
        }
    }
    return 0;
}
