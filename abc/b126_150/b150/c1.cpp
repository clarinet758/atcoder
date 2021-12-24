#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)


int main(){
    int n,x,y,cnt=0;
    sc1(n);
    vector <int> w,a(n),b(n);

    rep(i,n) w.push_back(i+1);
    rep(i,n) cin >> a.at(i);
    rep(i,n) cin >> b.at(i);
    do {
        cnt++;
        bool f=1;
        rep(i,n)  if (w.at(i) != a.at(i)) f=0;
        if (f) x=cnt;
        f=1;
        rep(i,n)  if (w.at(i) != b.at(i)) f=0;
        if (f) y=cnt;
    } while (next_permutation(w.begin(),w.end()));
    printf("%d\n",abs(x-y));
    return 0;
}
