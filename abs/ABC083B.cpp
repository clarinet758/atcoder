#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,a,b,chk,ans=0;
    sc3(n,a,b);
    rep(i,n+1) {
        chk=i/10000 + i%10000/1000 + i%1000/100 + i%100/10 + i%10;
        if (a<=chk && b>=chk) ans+=i;
    }
    cout << ans << endl;
   
    return 0;
}
