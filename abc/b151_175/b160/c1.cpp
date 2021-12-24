#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int mod=1000000007;
    int k,n,x=0,ans;
    sc2(k,n);
    vector <int> a(n);
    rep(i,n) {
        cin >> a.at(i);
        if (i>0)  x=max(x,a.at(i)-a.at(i-1));
    }
    x=max(x,a.at(0)+k-a.at(n-1));
    printf("%d\n",k-x);
    return 0;
}
