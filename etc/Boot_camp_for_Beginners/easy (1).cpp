#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int a,b,ans=0;
    sc2(a,b);
    b-=1;
    while(b>0) {
        ans++;
        b-=(a-1);
    }
    cout << ans << endl;
    return 0;
}
